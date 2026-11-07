"""Crosswalk lookup and validation for the HS3 clause-mapping pilot.

Usage:
  python3 09_map_lookup.py <coding.csv> <clause_dictionary.csv> <crosswalk.csv> <annexA.csv> <out_dir>

What it does (deterministic, no network):
  1. Checks every coded clause_id exists in the clause dictionary (catches typos).
  2. Checks every evidenced link has a quote anchor.
  3. For each AI RMF link, looks up ISO/IEC 42001 targets in the NIST crosswalk and converts
     Annex B numbers (B.x) to the matching Annex A control (A.x); main-body clauses stay as "Cl. x".
  4. Checks every converted Annex A control exists in the Annex A list.
  5. Writes mapped_records.csv and validation_report.txt, sorted, with fixed line endings.
"""
import csv
import os
import sys


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(coding, dictionary, crosswalk, annex, out_dir):
    clauses = {r["clause_id"]: r for r in read_csv(dictionary)}
    xwalk = {r["ai_rmf_id"]: r["crosswalk_targets_as_listed"].split(";") for r in read_csv(crosswalk)}
    annex_ids = {r["control_id"]: r["title"] for r in read_csv(annex)}
    rows = read_csv(coding)

    problems, out = [], []
    for r in rows:
        cid = r["clause_id"]
        iso, iso_note = "", ""
        if cid not in ("NONE", "-"):
            if cid not in clauses:
                problems.append(f"T#{r['tracker_row']} {r['framework']}: clause '{cid}' not in dictionary")
            if r["link_basis"] == "evidenced" and not r["quote_anchor"].strip():
                problems.append(f"T#{r['tracker_row']} {cid}: evidenced link has no quote anchor")
            if r["framework"] == "AI RMF":
                targets = xwalk.get(cid)
                if targets is None:
                    problems.append(f"T#{r['tracker_row']} {cid}: no crosswalk entry")
                else:
                    conv = []
                    for t in targets:
                        if t.startswith("B."):
                            a = "A." + t[2:]
                            if a not in annex_ids:
                                problems.append(f"T#{r['tracker_row']} {cid}: crosswalk target {t} -> {a} not in Annex A list")
                            conv.append(a)
                        else:
                            conv.append("Cl. " + t)
                    iso = "; ".join(conv)
                    iso_note = f"{len(conv)} targets" + (" (too broad to trace one control)" if len(conv) > 4 else "")
        out.append({
            "tracker_row": r["tracker_row"], "short_ref": r["short_ref"], "codable": r["codable"],
            "role": r["role"], "framework": r["framework"], "clause_id": cid,
            "clause_text": clauses.get(cid, {}).get("official_text", ""),
            "link_basis": r["link_basis"], "quote_anchor": r["quote_anchor"], "confidence": r["confidence"],
            "iso42001_via_crosswalk": iso, "iso_note": iso_note,
        })

    out.sort(key=lambda x: (int(x["tracker_row"]), x["framework"]))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "mapped_records.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(out)

    sources = sorted({r["tracker_row"] for r in rows}, key=int)
    codable = sorted({r["tracker_row"] for r in rows if r["codable"] == "Y"}, key=int)
    links = [r for r in rows if r["clause_id"] not in ("NONE", "-")]
    nones = [r for r in rows if r["clause_id"] == "NONE"]
    with open(os.path.join(out_dir, "validation_report.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"sources={len(sources)}\n")
        f.write(f"codable={len(codable)} ({','.join(codable)})\n")
        f.write(f"assigned_links={len(links)}\n")
        f.write(f"unresolved_NONE={len(nones)}\n")
        f.write(f"problems={len(problems)}\n")
        for p in problems:
            f.write(f"  - {p}\n")


if __name__ == "__main__":
    if len(sys.argv) != 6:
        sys.exit(__doc__)
    main(*sys.argv[1:])
