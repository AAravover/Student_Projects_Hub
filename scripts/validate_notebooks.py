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
    for cell in cells:
        if cell.get("cell_type") == "markdown":
            src = "".join(cell.get("source") or [])
            for ln in (l.strip() for l in src.splitlines()):
                if ln:
                    return True, ln  # dataset name
            return False, "first markdown cell is empty"

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
