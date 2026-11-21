"""Re-test of the role-of-AI pattern (A12, feedback item on the contribution), independent of the
Assignment 09 role assignment.

Usage:
  python analysis/role_retest.py audit/a12/03_fulltext_coding_claude.csv mapping/a09_proof_map_links.csv <out_dir>

Pattern under test (thesis A11, Section 4.4.4): for defence-tool AI (D) the operational clause sits in
NIST CSF 2.0 and AI-framework clauses cover only the tool's own trustworthiness; for the organization's
own AI (O) the AI RMF has direct clauses; for attacker AI (A) no AI RMF clause applies.

Here the role is the one coded per control from the full text (rule v1.2), without the Assignment 09
role, and only verdicts under rule v1.2 count. Refutation test fixed in A11: the pattern fails if a
control coded D has a Supported AI RMF link, or a control coded O has no AI-framework link at all.
Writes role_retest.txt. No network access.
"""
import csv
import os
import sys
from collections import Counter

AI_RMF = ("GOVERN", "MAP", "MEASURE", "MANAGE")


def verdict(v):
    v = v.lower()
    if v.startswith("supported"):
        return "S"
    if v.startswith("partly"):
        return "P"
    if v.startswith("evidenced gap"):
        return "gap"
    if v.startswith("not supported"):
        return "NS"
    return "none"


def main(coded_csv, a09_csv, out_dir):
    a09 = {r["link_id"]: r["role_a09"] for r in csv.DictReader(open(a09_csv, newline="", encoding="utf-8"))}
    rows = list(csv.DictReader(open(coded_csv, newline="", encoding="utf-8")))
    lines = []
    full = [r for r in rows if r["location"] != "abstract"]
    lines.append(f"links={len(rows)} full_text_links={len(full)}")
    changed = [r for r in rows if r["role_fresh_claude"] in "DOA" and r["role_fresh_claude"] != a09[r["link_id"]]]
    lines.append(f"role changed vs Assignment 09 (per-control, full text): {len(changed)} of {sum(r['role_fresh_claude'] in 'DOA' for r in rows)} coded links")
    for r in changed:
        lines.append(f"  {r['link_id']} T#{r['tracker_row']} {r['clause_id']}: {a09[r['link_id']]} -> {r['role_fresh_claude']}")
    lines.append("")
    lines.append("verdicts by fresh role and framework (S=Supported P=Partly NS=Not supported gap=evidenced gap none=not evidenced)")
    for scope, subset in (("all links", rows), ("full-text links only", full)):
        lines.append(f"[{scope}]")
        for role in ("D", "O", "A"):
            for fw in ("AI RMF", "CSF"):
                c = Counter(verdict(r["claude_verdict_v12"]) for r in subset
                            if r["role_fresh_claude"] == role and (r["clause_id"].startswith(AI_RMF) == (fw == "AI RMF")))
                lines.append(f"  role {role} {fw}: " + (", ".join(f"{k}={c[k]}" for k in ("S", "P", "NS", "gap", "none") if c[k]) or "no links"))
    d_ai_s = [r["link_id"] for r in rows if r["role_fresh_claude"] == "D" and r["clause_id"].startswith(AI_RMF) and verdict(r["claude_verdict_v12"]) == "S"]
    o_src = {r["tracker_row"] for r in rows if r["role_fresh_claude"] == "O"}
    o_no_ai = sorted(s for s in o_src if not any(r["tracker_row"] == s and r["role_fresh_claude"] == "O" and r["clause_id"].startswith(AI_RMF) and verdict(r["claude_verdict_v12"]) in ("S", "P") for r in rows))
    lines.append("")
    lines.append(f"refutation check 1 - D control with Supported AI RMF link: {d_ai_s if d_ai_s else 'none'}")
    lines.append(f"refutation check 2 - sources with O controls but no Supported/Partly AI RMF link: {['T#' + s for s in o_no_ai] if o_no_ai else 'none'}")
    a_links = [r["link_id"] for r in rows if r["role_fresh_claude"] == "A"]
    lines.append(f"links whose control is coded A: {a_links if a_links else 'none'}")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "role_retest.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
