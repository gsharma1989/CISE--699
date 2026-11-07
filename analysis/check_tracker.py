"""Integrity and consistency checks on the screening tracker (audit check A2).

Usage:
  python3 analysis/check_tracker.py screening/Screening_Tracker_Full_Scale.xlsx <out_dir> [identifiers.csv]

Checks (no network):
  1. IDs run 1..N with no gaps (IDs from row 13 on are the formula =ROW()-1).
  2. Every logged row has title, authors, year, database/source, source type, category,
     decision, reason and date; decision is Include or Exclude; category is one of the seven.
  3. Dates are YYYY-MM-DD; OpenAlex rows (R3, IDs 25+) have years 2023-2026 (the query limit).
  4. Reasons are at least 40 characters (the tracker rule: no one-word reasons).
  5. Duplicate titles (case and punctuation ignored).
  6. Spot-Check Log: every row number exists and its 'Original Decision' equals the tracker.
  7. Spot-Check Log notes still marked 'not yet confirmed by me'.
  8. If identifiers.csv is given: duplicate DOIs or OpenAlex IDs.
Writes integrity_report.txt; each finding is a line starting with WARN or INFO.
"""
import csv
import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rebuild_counts import CATEGORIES, load  # noqa: E402


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def main(xlsx, out_dir, ident=None):
    rows = load(xlsx)
    lines = []
    ids = [r["id"] for r in rows]
    if ids != list(range(1, len(rows) + 1)):
        lines.append(f"WARN ids not contiguous: {ids}")
    need = ["title", "authors", "year", "database_source", "source_type", "category",
            "decision", "reason", "date_screened"]
    for r in rows:
        for k in need:
            if not str(r[k] or "").strip() or str(r[k]) == "None":
                lines.append(f"WARN T#{r['id']}: empty {k}")
        if r["decision"] not in ("Include", "Exclude"):
            lines.append(f"WARN T#{r['id']}: decision {r['decision']!r}")
        if r["category"] not in CATEGORIES:
            lines.append(f"WARN T#{r['id']}: category {r['category']!r}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["date_screened"]):
            lines.append(f"WARN T#{r['id']}: date {r['date_screened']!r}")
        if r["id"] >= 25 and not ("2023" <= r["year"] <= "2026"):
            lines.append(f"WARN T#{r['id']}: year {r['year']} outside the OpenAlex query limit 2023-2026")
        if len((r["reason"] or "").strip()) < 40:
            lines.append(f"WARN T#{r['id']}: reason shorter than 40 characters")
    seen = {}
    for r in rows:
        seen.setdefault(norm(r["title"]), []).append(r["id"])
    for t, group in sorted(seen.items(), key=lambda x: x[1]):
        if len(group) > 1:
            explained = all("duplicate" in (rows[i - 1]["reason"] or "").lower() or "identical title" in (rows[i - 1]["reason"] or "").lower() for i in group[1:])
            lines.append(f"{'INFO' if explained else 'WARN'} duplicate title in T#{group}: '{t[:60]}'" + (" (explained in the reason column)" if explained else ""))
    by_id = {r["id"]: r for r in rows}
    ws = openpyxl.load_workbook(xlsx)["Spot-Check Log"]
    for r in range(2, ws.max_row + 1):
        ref, orig, note = ws.cell(r, 1).value, ws.cell(r, 3).value, ws.cell(r, 6).value or ""
        m = re.fullmatch(r"#(\d+)", str(ref or "").strip())
        if not m:
            continue
        i = int(m.group(1))
        if i not in by_id:
            lines.append(f"WARN spot-check row {r}: T#{i} not in tracker")
        elif orig != by_id[i]["decision"]:
            lines.append(f"WARN spot-check row {r}: T#{i} original decision {orig!r} but tracker says {by_id[i]['decision']!r}")
        if "not yet confirmed by me" in note:
            lines.append(f"WARN spot-check row {r}: T#{i} re-check still marked 'not yet confirmed by me'")
    if ident:
        with open(ident, newline="", encoding="utf-8") as f:
            idr = list(csv.DictReader(f))
        for key in ("doi", "openalex_id"):
            vals = {}
            for x in idr:
                v = (x.get(key) or "").strip().lower()
                if v and v != "none":
                    vals.setdefault(v, []).append(x["id"])
            for v, g in sorted(vals.items()):
                if len(g) > 1:
                    lines.append(f"WARN duplicate {key} {v} in T#{g}")
    lines.append(f"INFO rows checked: {len(rows)}; warnings: {sum(l.startswith('WARN') for l in lines)}")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "integrity_report.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    main(*sys.argv[1:])
