# 09 Re-audit of results changed since the Hard Stop 5 record

**Scope.** As the A12 brief asks, this audit covers only results that changed after the audited record. The audited record is hs5-rc2, carried into a11-evidence-v1. Unchanged results keep their HS5 audit status.

**Record versions.**
- Baseline: a11-evidence-v1 (commit 82059ee).
- New: a12-evidence-v1, which contains this folder.

## Changed results

| ID | Result | Before (a11-evidence-v1) | Now (a12-evidence-v1) | How it was re-audited | Status |
|---|---|---|---|---|---|
| C1 | Corpus counts | 60 logged, 45 included, 15 excluded; 12 included not peer reviewed | 80 logged, 56 included, 24 excluded; 17 not peer reviewed. The 45 Round 1-3 sources stay the analysis corpus for mapping. | `rebuild_counts.py` and `check_tracker.py` rerun: 0 warnings; the duplicate (rows 68/75) is explained. The R4 decisions were proposed by Claude. | Settled. R4 decisions reviewed and agreed by Gaurav on 2026-11-20, not blind (`08_atlas_author_review_NOTE.md`); R4 tiers reviewed by Gaurav (three changed: rows 61, 65, 79). |
| C2 | Clause-link verdicts | Abstract level: 22 of 43 links anchored. Author retrace: 1 of 22 Supported. Claude: 10 of 22. Kappa 0.06. | Full text for 28 links in 8 sources, under rule v1.2 (fixed before coding): 6 Supported, 14 Partly, 7 Not supported, 1 evidenced gap. 15 links in 5 sources have no full text and keep their abstract-level verdicts. | Rule and worked examples saved before coding (`01`, `03_..._SAVED_AT.txt`). Claude made the first pass. Gaurav reviewed it and agreed (not blind, not independent: `04_..._NOTE.md`). | Provisional. Not second-coded by another human. |
| C3 | Reliability of role coding | v1.1: 13 of 13 on non-fresh rows (author vs Claude) | Fresh sample of 8, independent second human reader (Sanjeev Tiwari): codability 7 of 8, kappa 0.60; main role 4 of 6, kappa 0.43. 3 disagreements resolved with written reasons; original answers kept. | `05_agreement.py` rerun; inputs saved before discussion | Settled as measured. The target (7 of 8) was not met. |
| C4 | Role-of-AI pattern | Provisional hypothesis | Not supported as a finding about the literature. Kept only as a heuristic derived from framework scope. | `role_retest.py` (new) on per-control full-text roles, plus C3 | Settled (negative result) |
| C5 | "No source builds the full chain" | Settled for the 45-source corpus | Narrowed: no **peer-reviewed** source among the 56 does so with evidence for each link. Two 2026 repository artefacts claim such mappings but cannot be verified. | `08_atlas_chain_check.md`; 4 sources read (record or full text) | Settled as narrowed |
| C6 | Appraisal of review-type sources | Tier rule only; AMSTAR 2 pending | Adapted AMSTAR 2 applied to 12 review-type sources. Suitable and appraisable: 3 systematic reviews, all critically low confidence. Not suitable (narrative or survey): 4. Not readable or not determined: 5. Tiers unchanged. | `07_review_appraisal.csv`; full text or abstract read by web-fetch | Settled for the readable sources |
| C7 | Reproduction | Run 2 by the author on Windows: ALL OUTPUTS MATCH | Run 3 by a person other than the author, from a fresh download: ALL OUTPUTS MATCH (same laptop and Python) | `11_run3_independent_rerun.md`, screenshots, signed log | Settled. A different computer is still pending. |
| C8 | PRISMA 2020 reporting | Not assessed | 42 items: 30 met (including one met by a statement), 8 partly met, 2 not met (items 14 and 21, reporting bias), 2 not applicable | `06_prisma2020_checklist.csv` | Settled |

## Expected outputs for a12-evidence-v1

| File | Change |
|---|---|
| `counts.txt` | Changed because of C1 |
| `integrity_report.txt` | Changed because of C1 |
| `tracker_rows.csv` | Changed because of C1 |
| `role_retest.txt` | New (C4) |
| `iso_comparison.csv` | Unchanged (MATCH) |
| `sensitivity.txt` | Unchanged (MATCH) |

New SHA-256 values are in `audit/a12/expected_outputs.txt`.

## Not re-audited (unchanged since HS5)

- ISO crosswalk comparison.
- Abstract-level sensitivity table (Display 7 of A11).
- Citation validation of the 44 A11 references. Only the new references were checked.
- Screening decisions for rows 1-60.
