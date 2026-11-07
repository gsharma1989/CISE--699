"""Sensitivity check (audit check A7): does the role-of-AI pattern in Assignment 09 Display 2 hold
when only evidenced links count, and when non-peer-reviewed sources are removed?

Usage:
  python3 analysis/sensitivity.py <tracker_rows.csv from rebuild_counts.py> mapping/a09_proof_map_links.csv <out_dir>

For each role (D, O, A) it counts the Display 2 sources, and how many have at least one link to the
NIST AI RMF and to NIST CSF 2.0 under three readings:
  as published  - every link listed in Assignment 09
  evidenced     - only links with a quote anchor in the public abstract (Codebook v1.1)
  evidenced, peer-reviewed only - as above, dropping sources flagged 'not peer reviewed'
Writes sensitivity.txt. No network access.
"""
import csv
import os
import sys


def main(rows_csv, links_csv, out_dir):
    flag = {r["id"]: r["peer_review_flag"] for r in csv.DictReader(open(rows_csv, newline="", encoding="utf-8"))}
    links = list(csv.DictReader(open(links_csv, newline="", encoding="utf-8")))
    srcs = {}
    for l in links:
        srcs.setdefault(l["tracker_row"], {"role": l["role_a09"], "ref": l["short_ref"], "links": []})["links"].append(l)
    lines = []
    for label, keep_link, keep_src in [
        ("as published", lambda l: True, lambda s: True),
        ("evidenced", lambda l: l["link_basis_v11"].startswith("evidenced"), lambda s: True),
        ("evidenced, peer-reviewed only", lambda l: l["link_basis_v11"].startswith("evidenced"), lambda s: flag[s] != "not peer reviewed"),
    ]:
        lines.append(f"[{label}]")
        for role in ("D", "O", "A"):
            ids = [s for s, v in srcs.items() if v["role"] == role and keep_src(s)]
            ai = [s for s in ids if any(keep_link(l) and l["framework"] == "AI RMF" for l in srcs[s]["links"])]
            csf = [s for s in ids if any(keep_link(l) and l["framework"] == "CSF" for l in srcs[s]["links"])]
            lines.append(f"  role {role}: sources={len(ids)} with_AI_RMF_link={len(ai)} ({','.join(sorted(ai, key=int))}) with_CSF_link={len(csf)} ({','.join(sorted(csf, key=int))})")
    dropped = sorted({s for s in srcs if flag[s] == "not peer reviewed"}, key=int)
    lines.append(f"sources dropped as not peer reviewed: {','.join(dropped) if dropped else 'none'}")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "sensitivity.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
