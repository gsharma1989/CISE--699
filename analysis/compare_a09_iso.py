"""Compare the ISO/IEC 42001 controls listed in Assignment 09 Display 2 with the full NIST crosswalk.

Usage:
  python3 analysis/compare_a09_iso.py mapping/a09_proof_map_links.csv \
      pilot/hs3-mapping-pilot/04_crosswalk_ai-rmf_to_iso42001.csv \
      pilot/hs3-mapping-pilot/05_annexA_controls.csv <out_dir>

For every AI RMF link it converts the crosswalk targets (Annex B number B.x -> Annex A control A.x;
main-body clauses shown as 'Cl. x'), checks each A.x exists in the Annex A list, and reports
whether the Assignment 09 entry listed all targets, a subset, or something else.
Writes iso_comparison.csv. No network access.
"""
import csv
import os
import re
import sys


def main(links, crosswalk, annex, out_dir):
    xw = {r["ai_rmf_id"]: r["crosswalk_targets_as_listed"].split(";") for r in csv.DictReader(open(crosswalk, newline="", encoding="utf-8"))}
    annex_ids = {r["control_id"] for r in csv.DictReader(open(annex, newline="", encoding="utf-8"))}
    out = []
    for r in csv.DictReader(open(links, newline="", encoding="utf-8")):
        if r["framework"] != "AI RMF":
            continue
        full = []
        for t in xw.get(r["clause_id"], []):
            if t.startswith("B."):
                a = "A." + t[2:]
                full.append(a if a in annex_ids else a + "(?)")
            else:
                full.append("Cl. " + t)
        listed = set(re.findall(r"A\.\d+(?:\.\d+)*", r["a09_iso_listed"]))
        full_a = {x for x in full if x.startswith("A.")}
        if not r["a09_iso_listed"].strip() or r["a09_iso_listed"].startswith(("(", "Broad", "7 controls")):
            status = "not listed separately in Assignment 09"
        elif not full_a:
            status = "main-body clauses only; all listed"
        elif listed == full_a:
            status = "all Annex A targets listed"
        elif listed < full_a:
            status = f"subset: {len(listed)} of {len(full_a)} Annex A targets listed"
        else:
            status = "lists controls not in the crosswalk for this clause: " + "; ".join(sorted(listed - full_a))
        out.append({"link_id": r["link_id"], "tracker_row": r["tracker_row"], "clause_id": r["clause_id"],
                    "a09_iso_listed": r["a09_iso_listed"], "crosswalk_full": "; ".join(full), "status": status})
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "iso_comparison.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(out)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main(*sys.argv[1:])
