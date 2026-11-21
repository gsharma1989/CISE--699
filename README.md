# Research materials: AI-Driven Cybersecurity Risk Management (CISE 699 thesis)

Gaurav Sharma, Harrisburg University of Science and Technology. Supervisor: Dr. Majid Shaalan.
Method: PRISMA 2020 systematic literature review with narrative synthesis and a clause-level governance mapping.
Release: **a12-evidence-v1** (2026-11-20): the evidence version for the Assignment 12 (Hard Stop 6) near-final thesis. It is `a11-evidence-v1` plus the A12 work asked for in the A11 feedback (`audit/a12/`, start with `00_plan.md` and `10_response_matrix.md`), Round 4 tracker rows 61-80, and three new scripts (`role_retest.py`, `fig_tiers.py`, `fig_chain.py`). Earlier frozen states: `v1.0-baseline`, `hs3-thesis-v2.0`, `hs5-rc1`, `hs5-rc2`, `a11-evidence-v1`.

## 1. Purpose
The review asks what published research shows about tracing AI-related cybersecurity threats to specific controls and then to named clauses in NIST AI RMF 1.0, ISO/IEC 42001 and NIST CSF 2.0. This repository holds everything needed to examine how the findings were produced and to rebuild every count.

## 2. Principal claims and where to check them
| Claim (thesis A12) | Records | How to check | Status |
|---|---|---|---|
| C1. 80 logged, 56 included, 24 excluded; 17 included not peer reviewed | `screening/Screening_Tracker_Full_Scale.xlsx` | Step 2 rebuilds `counts.txt` | Settled; rows 61-80 proposed by Claude and reviewed by the author on 2026-11-20 (not blind), tiers reviewed by the author |
| C2. Full-text clause links: 6 of 28 Supported, 14 Partly, 7 Not supported, 1 evidenced gap | `audit/a12/01_supported_rule.md`, `03_fulltext_coding_claude.csv` | Read the rule, then the anchors | Provisional (author review, no independent second coder) |
| C3. Second reader, fresh sample: control named 7/8 (kappa 0.60); role 4/6 (kappa 0.43) | `audit/a12/05_*` | `python audit/a12/05_agreement.py audit/a12/05_fresh_coding_sanjeev.csv audit/a12/05_fresh_coding_claude.csv` | Settled as measured |
| C4. The role-of-AI pattern is not supported as a finding | `audit/a12/12_role_retest.md` | Step 4c, `out/role_retest.txt` | Settled (negative result) |
| C5. No peer-reviewed source traces threat -> control -> numbered clause with evidence | `audit/a12/08_atlas_*` | Read the chain check | Settled as narrowed |
| C6. AMSTAR 2 where it fits; PRISMA 2020 checklist | `audit/a12/06_*`, `07_*` | Read the files | Settled |

## 3. Inventory
| Folder or file | What it is | Origin |
|---|---|---|
| `protocol/` | Review protocol (Assignment 1) | Written by me |
| `screening/Screening_Tracker_Full_Scale.xlsx` | All 80 screening decisions with reason, source, query and rank | Rows 1-12 by me; rows 13-60 proposed by Claude and reviewed by me; rows 61-80 proposed by Claude and reviewed by me (not blind) |
| `mapping/a09_proof_map_links.csv` | 43 proof-map links at Hard Stop 5 | Hard Stop 5 |
| `analysis/*.py` | Scripts: counts, integrity, ISO lists, sensitivity, role re-test, figures, output check | Written by Claude; outputs checked by hash; rerun by a person other than the author (Run 3) |
| `pilot/hs3-mapping-pilot/` | Hard Stop 3 clause-mapping pilot | See its README |
| `audit/hs5/`, `audit/a11/` | Hard Stop 5 audit; pre-A11 checks and Runs 1-2 | Earlier checkpoints |
| `audit/a12/` | A12: rule (01), full-text coding (02-04), second reader (05), PRISMA (06), AMSTAR 2 (07), MITRE ATLAS round (08), changed-results audit (09), response matrix (10), Run 3 (11), role re-test (12), Claude's unedited thesis draft (13), completed sheets (`sheets/`), expected outputs | This release |
| `logs/` | Risk log, known issues, changelog | Kept since Assignment 5 |

## 4. Provenance
- Searches: Google Scholar (rows 1-12, Oct 2026), targeted web searches (rows 13-24), OpenAlex queries A-D (rows 25-60; query text and rank in the tracker) and Query E "MITRE ATLAS" (rows 61-80; snapshot of ranks 1-50 in `audit/a12/08_atlas_snapshot.csv`, retrieved 2026-11-20). Dates are in the tracker.
- Clause wording: NIST AI Resource Center (AI RMF Core) and NIST CSF 2.0 Implementation Examples, copied word for word into `03_clause_dictionary.csv`. ISO/IEC 42001 controls come only from NIST's AI RMF-to-ISO/IEC FDIS 42001 crosswalk.
- AI assistance: Claude (Anthropic) proposed screening decisions for rows 13-80, made the first pass of the A12 full-text coding and AMSTAR 2 sheet, wrote the scripts and summaries, and drafted text. Every use is logged in the AI-use section of each memo. Commit history on GitHub shows the order of work; audit plans were committed before checks were run.

## 5. Prerequisites
Python 3.10 or later with `openpyxl` 3.1.5. Tested on Linux (Python 3.13) and Windows 11 (Python 3.15.2, Runs 2 and 3). Step 1 needs network access once; the other steps need none. The figure scripts (optional Step 6) also need `matplotlib`.

## 6. Steps (run from the repository root)
```
python3 -m venv .venv && . .venv/bin/activate && pip install openpyxl==3.1.5      # Step 1
python3 analysis/rebuild_counts.py screening/Screening_Tracker_Full_Scale.xlsx out   # Step 2: counts.txt, tracker_rows.csv
python3 analysis/check_tracker.py screening/Screening_Tracker_Full_Scale.xlsx out    # Step 3: integrity_report.txt
python3 analysis/compare_a09_iso.py mapping/a09_proof_map_links.csv pilot/hs3-mapping-pilot/04_crosswalk_ai-rmf_to_iso42001.csv pilot/hs3-mapping-pilot/05_annexA_controls.csv out   # Step 4a
python3 analysis/sensitivity.py out/tracker_rows.csv mapping/a09_proof_map_links.csv out   # Step 4b
python3 analysis/role_retest.py audit/a12/03_fulltext_coding_claude.csv mapping/a09_proof_map_links.csv out   # Step 4c (new in A12)
python3 analysis/verify_outputs.py out audit/a12/expected_outputs.txt   # Step 5: prints MATCH for each file
python3 analysis/fig_tiers.py . out/fig_tiers.png && python3 analysis/fig_chain.py out/fig_chain.png   # Step 6 (optional, needs matplotlib)
```
Expected results for this release: `counts.txt` reports logged=80, included=56, excluded=24, included_not_peer_reviewed=17; `integrity_report.txt` reports 80 rows and 0 warnings; `role_retest.txt` reports 5 of 41 roles changed and no D control with a Supported AI RMF link. Step 5 compares six files with `audit/a12/expected_outputs.txt` and should print **ALL OUTPUTS MATCH**. (The A11 values are still in `audit/a11/expected_outputs.txt`; three files differ by design, see `audit/a12/09_changed_results_audit.md`.)

### Windows, step by step (for a reviewer without Linux)
1. Install Python 3.10+ from python.org (tick "Add Python to PATH").
2. On GitHub, open Releases, choose **a12-evidence-v1**, download **Source code (zip)**. Right-click the zip, choose **Extract All**, then open the extracted folder until you see `README.md`, `analysis` and `screening`.
3. **Open a command window in that folder:** click once in the address bar at the top of the File Explorer window (where the folder path is shown), delete the text, type `cmd` and press Enter. A black window opens already inside the folder.
4. Check Python: type `py --version` and press Enter. It should print a version number.
5. Run: `py -m pip install openpyxl==3.1.5`
6. Run the commands of Steps 2 to 4c above one at a time, with `py` instead of `python3` (copy one line, right-click in the black window to paste, press Enter).
7. Run `py analysis/verify_outputs.py out audit/a12/expected_outputs.txt`. It should print **ALL OUTPUTS MATCH**.

## 7. Restrictions and safe access
- **Abstracts and full texts** are copyrighted and are not stored here. Each source is identified by DOI or OpenAlex ID (`audit/hs5/04_provenance_openalex.csv`), so a reviewer can retrieve the same abstract from OpenAlex or the publisher. Quote anchors are under 15 words.
- **ISO/IEC 42001** is a paid standard and I do not have a copy. ISO matches are provisional and come only from NIST's crosswalk (built on the draft FDIS). The crosswalk files are a substitute that shows the procedure; they do not verify ISO wording.
- **Paywalled sources** (for example Mokgathi & Ogundele 2026; Nolte et al. 2025) were checked on abstract and publisher metadata only.
- **No personal or organizational data** is used. Google Scholar was used only through its normal web interface; when it blocked paging, searching moved to OpenAlex instead of working around the block.

## 8. Known limitations
AI-assisted screening and coding with limited independent human checking (the 28 full-text verdicts have no independent second coder; Round 4 decisions were reviewed by the author, not blind); five mapped sources had no legal free full text; licensed databases were not searched; only Round 4 has a saved search snapshot; ISO matches are second-hand; Runs 2 and 3 used the same computer. See the thesis, Chapter 6, and `logs/know-issues.md`.
