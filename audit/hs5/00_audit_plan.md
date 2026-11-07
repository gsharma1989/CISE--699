# Hard Stop 5 Audit Plan (written before any audit check was run)

Date: 2026-11-07. Author: Gaurav Sharma, with Claude (Anthropic) as research assistant.
Starting point: release tag `hs3-thesis-v2.0` (commit 3338f1f) plus the Assignment 09 memo and tracker.

## Principal claims under audit
- **C1 (corpus):** 60 sources logged, 45 included, 15 excluded; counts by category as reported in Assignment 09 (Evidence Display 1); about 13 of 45 included sources are not peer reviewed.
- **C2 (proof map):** for 10 sources, a threat-to-control-to-clause chain can be built (Assignment 09, Evidence Display 2), and the framework that holds the clause depends on the role of AI (defence tool, own AI, attacker's tool).
- **C3 (pilot):** the clause-mapping procedure is repeatable for its mechanical steps, but clause links and role codes did not reach the pre-set thresholds (Hard Stop 3, tag hs3-thesis-v2.0).

## Checks and pass criteria (fixed now)
| ID | Check | Reviewer | Pass if |
|----|-------|----------|---------|
| A1 | Fresh computational run: rebuild C1 counts from the tagged tracker in a clean folder, following only the README | Claude (self-audit from written instructions; not independent) | Counts match the tracker formulas exactly; two runs byte-identical; any difference from numbers reported in Assignment 09 is logged |
| A2 | Tracker integrity: unique IDs, no duplicate DOIs/titles, every row has decision, reason, source, date | Script | 0 unexplained problems |
| A3 | Provenance: every DOI or ID in the tracker resolves in OpenAlex and its title matches the tracker | Script + Claude | Every mismatch explained or corrected |
| A4 | My independent review of the 38 screening decisions I had not yet checked (rows 13–60), blind to the recorded decision | Gaurav | Agreement at least 90% (R-02 target); every disagreement resolved and logged |
| A5 | Role coding of the 13 rows of Assignment 09 Display 2 under Codebook v1.1 Step 3, blind to the recorded roles | Gaurav (second reader) | At least 11 of 13 agree; otherwise the role pattern (C2) is reported as unconfirmed |
| A6 | Re-code the Display 2 clause links under Codebook v1.1 (evidenced vs rule-inferred), then my independent retrace of the main links | Claude codes; Gaurav retraces | At least 80% of retraced links Supported (v1.1 definition); rule-inferred links do not count as evidence |
| A7 | Sensitivity: recompute C1 category counts and the C2 role pattern without non-peer-reviewed sources | Script | Report whether the pattern still holds |
| A8 | Quality appraisal of all 45 included sources by a written tier rule; I check a random 20% sample | Claude codes; Gaurav checks 9 | Disagreements logged and resolved |

Independence: I (Gaurav) did not build the scripts or write the summaries I review; Claude did. My reviews are blind to the recorded answers but use Claude-written summaries, so they are partly independent, not independent replication. No external reviewer is available for this checkpoint.

Restricted material: abstracts are not copied (copyright); they are identified by OpenAlex ID and DOI. ISO/IEC 42001 is paid; ISO links come only from the NIST crosswalk and stay provisional. No personal or organizational data is used.
