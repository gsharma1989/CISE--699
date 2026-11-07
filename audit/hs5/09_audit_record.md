# Hard Stop 5 audit record (start here)

Audited release: **hs5-rc1** (commit 517b36c). Corrected release: **hs5-rc2**. Plan and pass marks: 00_audit_plan.md (committed before any check).
Reviewers: Gaurav Sharma (blind second reader: A4, A5, A6, A8; answers given in the chat between about 18:10 and 18:45 UTC); Claude, Anthropic (scripts, fresh runs, provenance look-ups, first-pass coding). No external reviewer.

| Check | What was done | Result vs pass mark | Verdict | Records |
|---|---|---|---|---|
| A1 Fresh run | Two clean folders, files downloaded from the hs5-rc1 tag, new venv with openpyxl 3.1.5, README Section 6 followed exactly (2026-11-07 18:25 UTC). Repeated on hs5-rc2 after fixes | Both runs exit 0; all 5 outputs match the expected SHA-256; runs byte-identical; every C1 number in Assignment 09 reproduced. One instruction error found (D8) | Pass (self-audit, not independent) | 05_fresh_run_log_rc1.txt, 05_fresh_run_log_rc2.txt, 05_expected_outputs_rc*.txt |
| A2 Integrity | check_tracker.py on rc1 | 2 warnings (D2) plus a structural risk found by reading the file (D1); 0 warnings on rc2 | Pass after fixes | out/integrity_report.txt; 07 |
| A3 Provenance | Each of 60 titles looked up in OpenAlex (and Crossref where missing), matched on title, authors and year | 55 matched; 5 not indexed (2 explained, 3 still need an identifier); 1 type change found (D3); 1 DOI variant (D9) | Pass with open items | 04_provenance_openalex.csv; 07 |
| A4 Screening review | I re-screened 38 rows blind from neutral summaries | 38 of 38 agree (target at least 90%) | Pass | 01, 02 |
| A5 Role coding | I coded the 13 Display 2 rows blind under v1.1 role rules | 13 of 13 agree (target at least 11) | Pass, with caveats (I wrote Assignment 09; Claude wrote the summaries) | 01, 03 |
| A6 Clause links | 43 links re-coded under v1.1; I retraced the 22 anchored links blind (NIST wording shown slightly shortened; full text in the clause dictionary) | 1 of 22 Supported by me (4.5%), 10 of 22 by Claude; agreement 12 of 22, kappa 0.06 (target at least 80% Supported) | **Fail** | mapping/a09_proof_map_links.csv; 06 |
| A7 Sensitivity | Counts and role pattern with evidenced links only, and without non-peer-reviewed sources | Defence-tool rows: CSF link evidenced for 5 of 6, AI RMF for 3 of 6. Own-AI rows: 2 of 4 have any evidenced link. Attacker rows: no AI RMF link (as predicted), CSF for 2 of 3. Dropping non-peer-reviewed sources removes only T#17 and changes no pattern | Reported | out/sensitivity.txt |
| A8 Quality appraisal | Written tier rule; all 45 included sources rated; I rated a random 9 blind | Tiers 1 / 2 / 3: 9 / 21 / 15. My blind tiers for the random 9 (seed 20261107: T#3, 13, 19, 23, 30, 37, 49, 51, 55) agree on 9 of 9 | Pass (a light appraisal; AMSTAR 2 still to do) | 08_appraisal_rule.md, 08_quality_appraisal.csv, 08_appraisal_check_A8.csv |

What the audit supports: the corpus numbers (C1) are correct and repeatable; the screening decisions hold up under my blind review; the role definitions are applied consistently on the Assignment 09 rows.
What it does not support: that the Assignment 09 clause links are evidenced by the sources. Abstract-level text rarely states controls at clause level, so C2 is downgraded to a set of candidate links until full texts are coded.
