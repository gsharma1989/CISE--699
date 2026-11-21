# 10 Response matrix: Assignment 11 feedback (Dr. Majid Shaalan)

**Status key.**
- **Completed:** the change is made and its evidence is in the record.
- **Reasoned disagreement:** done differently, for a stated reason.
- **Pending:** not done yet, and the related claim is narrowed.

| # | Feedback | Status | What I did | Where |
|---|---|---|---|---|
| P1.1 | Reopen the full texts for the 4.4.2-4.4.5 links | Completed | Opened free full texts for 8 of the 13 mapped sources (28 of 43 links). The other 5 had no legal free full text and are labelled abstract-only. | 3.8; Display 9; record 02, 03 |
| P1.2 | For each link, record the location, exact control, clause, anchor and an S/P/NS verdict | Completed | Every link has these fields, plus a fresh per-control role. | Record 03 |
| P1.3 | Apply the same action-and-object rule to every link | Completed | Rule v1.2 was fixed, with five worked examples, before any coding. One amendment (A1) was made before any human verdict and is logged. | 3.7; record 01 |
| P1.4 | Compare with Display 5 | Completed | Full text: 6 Supported, 14 Partly, 7 Not supported, 1 gap. Abstract-level retrace was 1 of 22 Supported. | 4.4.3, Display 9 |
| P1.5 | Keep ISO provisional | Completed | ISO targets are never given a verdict. They still come from the NIST crosswalk of the draft standard. | 4.4.5 |
| P2.1 | Put worked examples first | Completed | Five worked examples, one per verdict type, came before coding. | 3.7; record 01 |
| P2.2 | Have a second human reader code a fresh sample of 8 | Completed | A fresh random sample of 8 (seed 20261120) was coded independently by Sanjeev Tiwari, a co-worker. No classmate was available. | 3.8; record 05 |
| P2.3 | Report agreement, disagreements and kappa | Completed | Codability 7 of 8 (kappa 0.60). Role 4 of 6 (kappa 0.43), which misses the 7 of 8 target. All 3 disagreements are listed. | Display 10 |
| P2.4 | Resolve disagreements with written reasons and keep the original decisions | Completed | R1-R3 were resolved by Gaurav and Sanjeev with written reasons. Both sets of original answers are kept. | Record 05_resolutions |
| P3.1 | Complete the PRISMA 2020 checklist and mark unmet items | Completed | 42 items: 30 met, 8 partly met, 2 not met (reporting bias), 2 not applicable. | Appendix B; record 06 |
| P3.2 | Appraise review-type sources and check that AMSTAR 2 suits each design | Completed | 12 review-type sources assessed. AMSTAR 2 suits 3 systematic reviews, all rated critically low confidence. It does not suit 4 narrative reviews or surveys. 5 could not be read or classified. | 3.6, Display 2; record 07 |
| P3.3 | Screen MITRE ATLAS within the source limit | Completed / Reasoned disagreement | Snapshot of ranks 1-50 out of 608 records. Ranks 1-20 were screened as rows 61-80, which fills the 80-source cap: 11 included. I did not screen beyond the cap, so as to keep the protocol limit. | 3.3, 4.4.1; record 08 |
| P3.4 | Explain how the new sources change the conclusions | Completed | Conclusion 1 is unchanged. The gap claim is narrowed to peer-reviewed, evidenced mappings. The search-bias alternative is partly supported. | 4.4.1, 5.2 |
| P3.5 | Document the licensed-database limitation | Completed | Scopus, Web of Science, IEEE Xplore and ACM were not searched. The effect is stated: engineering venues may be under-represented. | 3.4, Display 1; 6 |
| P4.1 | Complete Appendix E with a dated author review and the actual changes | Pending (author) | The table is ready. Gaurav must write and date his own review and list the changes he made. | Appendix E |
| P4.2 | Preserve the AI draft, corrections and verification notes | Completed | First-pass files are time-stamped (SAVED_AT). Corrections and the review notes are kept. | Record 03-05; Appendix E |
| P4.3 | Add the figure scripts and displays to the next release | Completed | fig_tiers.py, fig_chain.py and role_retest.py are in `analysis/`, with the display data. | Release a12-evidence-v1 (analysis/) |
| P4.4 | Have a peer follow the README independently | Completed | Run 3 by Sanjeev Tiwari from a fresh download: ALL OUTPUTS MATCH. Commands, environment, outputs and the help he needed are all logged. | 3.8; record 11 |
| C1 | Conclusion 1 is strong | Kept | Restated. Supported by 28 full-text links and 11 new sources. | 7 |
| C2 | Re-test the role pattern independently; a negative result is acceptable | Completed (negative result) | Roles were re-coded per control from the full texts, plus the second reader. The pattern is not supported as a finding and is kept only as a heuristic derived from framework scope. | 4.4.4; record 12 |

## Remaining revisions before final submission

1. Done 2026-11-20: Gaurav reviewed the 20 Round 4 screening decisions and agreed with all (record 08). He then checked the 11 Round 4 tiers and changed three (rows 61, 65, 79).
2. Gaurav writes and dates his Appendix E review.
3. Gaurav records the 6-10 minute walkthrough.
4. The release a12-evidence-v1 is published on GitHub, and the Appendix A links are checked.
5. Optional, if time allows:
   - A second human reader for the 28 full-text link verdicts.
   - A rerun on a different computer.
   - Checking the ISO matches against the published ISO/IEC 42001 text (licensed).
