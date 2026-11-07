"""Rebuild the corpus counts (claim C1) from the screening tracker.

Usage:
  python3 analysis/rebuild_counts.py screening/Screening_Tracker_Full_Scale.xlsx <out_dir>

Reads the 'Screening Tracker' tab, freezes each row's ID (the tracker shows IDs with the
formula =ROW()-1 from row 13 on), and writes:
  tracker_rows.csv  - one line per logged source, IDs as plain numbers
  counts.txt        - totals, included sources by category, by screening round,
                      and by peer-review flag (rule below), with and without
                      non-peer-reviewed sources
No network access. Deterministic: sorted output, fixed line endings.

Peer-review flag rule (written for this audit, applied to the Source Type column):
  not peer reviewed = Source Type starts with Preprint, Repository article, Policy note,
  Practitioner, Conference abstract, or Book ( (a whole book, not a chapter).
"""
import csv
import os
import re
import sys

import openpyxl

CATEGORIES = ["AI-related threats", "Privacy risks", "Security risks",
              "Human/organizational risks", "Governance risks", "Compliance risks",
              "Security controls"]
NPR = re.compile(r"^(Preprint|Repository article|Policy note|Practitioner|Conference abstract|Book \()")
FIELDS = ["id", "title", "authors", "year", "database_source", "source_type",
          "category", "decision", "reason", "date_screened", "round", "peer_review_flag"]


def screening_round(i):
    if i <= 12:
        return "R1 Hard Stop 4 batch (Google Scholar)"
    if i <= 24:
        return "R2 targeted web searches"
    return "R3 OpenAlex queries"


def load(path):
    ws = openpyxl.load_workbook(path)["Screening Tracker"]
    rows = []
    for r in range(2, ws.max_row + 1):
        v = [ws.cell(r, c).value for c in range(1, 11)]
        if not v[1]:
            continue
        shown = v[0]
        if not (str(shown) == str(r - 1) or shown == "=ROW()-1"):
            raise SystemExit(f"row {r}: ID cell {shown!r} is neither {r-1} nor =ROW()-1")
        i = r - 1
        rows.append({
            "id": i, "title": v[1], "authors": v[2], "year": str(v[3]), "database_source": v[4],
            "source_type": v[5], "category": v[6], "decision": v[7], "reason": v[8],
            "date_screened": str(v[9]), "round": screening_round(i),
            "peer_review_flag": "not peer reviewed" if NPR.match(v[5] or "") else "peer reviewed or unclear",
        })
    return rows


def main(xlsx, out_dir):
    rows = load(xlsx)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "tracker_rows.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    inc = [r for r in rows if r["decision"] == "Include"]
    exc = [r for r in rows if r["decision"] == "Exclude"]
    inc_pr = [r for r in inc if r["peer_review_flag"] != "not peer reviewed"]
    out = [
        f"logged={len(rows)}",
        f"included={len(inc)}",
        f"excluded={len(exc)}",
        f"undecided={len(rows) - len(inc) - len(exc)}",
        f"with_reason={sum(1 for r in rows if (r['reason'] or '').strip())}",
        f"included_not_peer_reviewed={len(inc) - len(inc_pr)} ({','.join(str(r['id']) for r in inc if r['peer_review_flag'] == 'not peer reviewed')})",
        "",
        "included_by_category (all | peer-reviewed-or-unclear only)",
    ]
    for c in CATEGORIES:
        out.append(f"  {c}: {sum(r['category'] == c for r in inc)} | {sum(r['category'] == c for r in inc_pr)}")
    other = sorted({r['category'] for r in inc} - set(CATEGORIES))
    out.append(f"  other category values: {other if other else 'none'}")
    out.append("")
    out.append("by_round (logged / included)")
    for rd in sorted({r['round'] for r in rows}):
        out.append(f"  {rd}: {sum(r['round'] == rd for r in rows)} / {sum(r['round'] == rd for r in inc)}")
    with open(os.path.join(out_dir, "counts.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
