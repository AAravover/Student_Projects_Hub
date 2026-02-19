#!/usr/bin/env python3
"""Build a static showcase website from student Jupyter notebooks.

Behavior
- Walks year/course/student folders (e.g. `2026/*/*/*`) and finds `.ipynb` files
- Converts each notebook to a standalone HTML file with nbconvert
- Converts any README.md found in a student folder to HTML
- Generates a top-level `site/index.html` that lists all projects grouped by year/course

Designed to be run in CI (GitHub Actions) and locally for preview.
"""
from __future__ import annotations

import shutil
from pathlib import Path
import nbformat
from nbconvert import HTMLExporter
import markdown
import json
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "site"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9_-]", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def find_notebooks() -> list[dict]:
    projects = []
    for year_dir in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name.isdigit()):
        year = year_dir.name
        for course_dir in sorted(p for p in year_dir.iterdir() if p.is_dir()):
            course = course_dir.name
            # find notebooks anywhere under the course directory (no personal folders required)
            for nb in sorted(x for x in course_dir.rglob("*.ipynb") if ".ipynb_checkpoints" not in x.parts):
                projects.append({"year": year, "course": course, "notebook_path": nb})
    return projects


def extract_title_and_description(nb_node) -> tuple[str, str]:
    """Extract dataset name and a short description from the first markdown cell.

    Convention: the first non-empty line of the first markdown cell is the
    dataset name; the following non-empty paragraph (if any) is used as a
    short description.
    """
    dataset = "(unknown dataset)"
    desc = ""
    for cell in nb_node.cells:
        if cell.cell_type != "markdown":
            continue
        text = cell.source or ""
        lines = [l.rstrip() for l in text.splitlines()]
        # locate first non-empty line
        for i, ln in enumerate(lines):
            if ln.strip():
                dataset = re.sub(r"^#+\s*", "", ln).strip()
                # look for next non-empty line to serve as description
                for later in lines[i + 1 :]:
                    if later.strip():
                        desc = later.strip()
                        break
                return dataset, desc
    return dataset, desc


def extract_author(nb_node) -> str | None:
    """Return the Author/Group value from the notebook (first markdown cell), or None."""
    for cell in nb_node.cells:
        if cell.cell_type != "markdown":
            continue
        text = cell.source or ""
        for ln in (l.strip() for l in text.splitlines()):
            m = re.match(r"^(?:Author|Group)\s*:\s*(.+)$", ln, flags=re.I)
            if m:
                return m.group(1).strip()
        # only inspect the first markdown cell for author/group per convention
        break
    return None


def convert_notebook(nb_path: Path, out_path: Path) -> tuple[str, str, str | None]:
    """Convert notebook to HTML and return (dataset, short_description, author).

    `author` is the value of an `Author:` or `Group:` line in the first markdown cell
    (if present).
    """
    nb_node = nbformat.read(nb_path, as_version=4)
    dataset, desc = extract_title_and_description(nb_node)
    author = extract_author(nb_node)

    exporter = HTMLExporter()
    exporter.exclude_input = False
    exporter.exclude_output_prompt = True
    body, _ = exporter.from_notebook_node(nb_node)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(body, encoding="utf-8")
    return dataset, desc, author


def convert_markdown(md_path: Path, out_path: Path) -> str:
    html = markdown.markdown(md_path.read_text(encoding="utf-8"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding="utf-8")
    return html


INDEX_HTML = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Student Projects Hub</title>
    <link rel="stylesheet" href="assets/style.css">
  </head>
  <body>
    <header class="site-header">
      <div class="container">
        <h1>Student Projects Hub — Project showcase</h1>
        <p class="muted">Automatically generated on {date}</p>
      </div>
    </header>
    <main class="container">
    {content}
    </main>
    <footer class="container muted">Generated with Student_Projects_Hub · {year}</footer>
  </body>
</html>
"""


def make_index(projects: list[dict]) -> str:
    # Group by year/course, then by student (stable deterministic order).
    grouped: dict = {}
    for p in projects:
        key = (p["year"], p["course"])
        grouped.setdefault(key, []).append(p)

    parts = []
    for (year, course), items in sorted(grouped.items()):
        parts.append(f"<section class=course-group>\n  <h2>{year} / {course}</h2>")

        # group projects by student
        students: dict = {}
        for it in items:
            students.setdefault(it["student"], []).append(it)

        parts.append("  <div class=students-grid>")
        for student, proj_list in sorted(students.items()):
            parts.append(f"    <div class=student>\n      <h3 class=student-name>{student.replace('_',' ').title()}</h3>\n      <div class=student-projects>")
            for pr in sorted(proj_list, key=lambda x: x["filename"]):
                parts.append(
                    "        <article class='project'>\n"
                    f"          <h4 class='proj-title'><a href='{pr['link']}'>{pr.get('title') or pr['filename']}</a></h4>\n"
                    f"          <p class='meta'>file: <span class='filename'>{pr['filename']}</span></p>\n"
                    f"          <p class='dataset'>dataset: <strong>{pr.get('dataset','')}</strong></p>\n"
                    f"          <p class='desc'>{(pr.get('desc') or '')}</p>\n"
                    "        </article>"
                )
            parts.append("      </div>\n    </div>")
        parts.append("  </div>\n</section>")

    return INDEX_HTML.format(content="\n".join(parts), date=datetime.utcnow().isoformat(), year=datetime.utcnow().year)


def copy_static():
    assets_src = ROOT / "site_src" / "assets"
    assets_dst = OUT_DIR / "assets"
    if assets_src.exists():
        if assets_dst.exists():
            shutil.rmtree(assets_dst)
        shutil.copytree(assets_src, assets_dst)


def build() -> int:
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    # ensure GitHub Pages doesn't run Jekyll processing
    (OUT_DIR / ".nojekyll").write_text("")

    copy_static()

    found = find_notebooks()
    built = []

    for entry in found:
        nb_path: Path = entry["notebook_path"]
        # preserve any subfolder structure under the course directory; place
        # output under site/<year>/<course>/[optional-subfolder]/<notebook>.html
        course_root = ROOT / entry["year"] / entry["course"]
        try:
            rel = nb_path.relative_to(course_root)
        except Exception:
            # fallback to using the notebook parent name
            rel = nb_path.name
        rel_out_dir = Path(entry["year"]) / entry["course"] / Path(rel).parent
        out_html = OUT_DIR / rel_out_dir / (nb_path.stem + ".html")

        dataset, desc, author = convert_notebook(nb_path, out_html)

        # also convert README.md if present in same folder
        readme = nb_path.parent / "README.md"
        if readme.exists():
            convert_markdown(readme, OUT_DIR / rel_out_dir / "README.html")

        entry["dataset"] = dataset
        entry["desc"] = desc
        entry["filename"] = nb_path.name
        # extract student/group from notebook (fallback to filename stem)
        entry["student"] = author or nb_path.stem
        # keep a display title (fallback to filename stem)
        entry["title"] = nb_path.stem
        # link from site root
        entry["link"] = str(rel_out_dir / (nb_path.stem + ".html"))
        built.append(entry)

    index_html = make_index(built)
    (OUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    print(f"Built {len(built)} notebook pages into {OUT_DIR!s}")
    return 0


if __name__ == "__main__":
    raise SystemExit(build())
