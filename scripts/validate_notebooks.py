#!/usr/bin/env python3
"""Validate student notebooks for the site generator conventions.

Checks performed:
- notebooks are valid JSON
- notebook contains at least one markdown cell
- the first markdown cell has a non-empty first line (dataset name)

Exit code 0 on success, non-zero on failure.
"""
from __future__ import annotations

import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate_notebook(path: Path) -> tuple[bool, str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return False, f"invalid JSON: {e}"

    cells = data.get("cells") or []
    # find first markdown cell
    import re

    for cell in cells:
        if cell.get("cell_type") == "markdown":
            src = "".join(cell.get("source") or [])
            lines = [l.strip() for l in src.splitlines()]

            # first non-empty line is the dataset name
            dataset = next((ln for ln in lines if ln), None)
            if not dataset:
                return False, "first markdown cell is empty"

            # require an Author: or Group: line in the first markdown cell
            author = None
            for ln in lines:
                m = re.match(r"^(?:Author|Group)\s*:\s*(.+)$", ln, flags=re.I)
                if m:
                    author = m.group(1).strip()
                    break
            if not author:
                return False, "missing 'Author:' or 'Group:' line in the first markdown cell"

            return True, f"dataset={dataset}; author={author}"

    return False, "no markdown cells found"


def main() -> int:
    failures = []
    checked = 0
    for nb in sorted(ROOT.glob("**/*.ipynb")):
        # skip any tooling notebooks not under year/course folders? keep all
        checked += 1
        ok, msg = validate_notebook(nb)
        if not ok:
            failures.append((nb, msg))

    print(f"Checked {checked} notebooks")
    if failures:
        print("\nValidation failures:")
        for p, reason in failures:
            print(f" - {p.relative_to(ROOT)}: {reason}")
        return 2

    print("All notebooks look good (first markdown cell contains dataset name)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
