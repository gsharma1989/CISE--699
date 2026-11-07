# Research materials: AI-Driven Cybersecurity Risk Management (CISE 699 thesis)

Gaurav Sharma, Harrisburg University of Technology. Supervisor: Dr. Majid Shaalan.
Method: PRISMA 2020 systematic literature review with narrative synthesis and a clause-level governance mapping.
Release: **hs5-rc2** (Hard Stop 5 submission, 2026-11-07): release candidate `hs5-rc1` after its audit and corrections. Earlier frozen states: `v1.0-baseline`, `hs3-thesis-v2.0`, `hs5-rc1`.

## 1. Purpose
The review asks what published research shows about tracing AI-related cybersecurity threats to specific controls and then to named clauses in NIST AI RMF 1.0, ISO/IEC 42001 and NIST CSF 2.0. This repository holds everything needed to examine how the findings so far were obtained: the protocol, every screening decision, the clause-mapping records, the scripts that rebuild the numbers, and the audit records. It is a research record, not software; the scripts only recount and cross-check the records.

## 2. Principal claims and where to check them
| Claim (where it was made) | Records | How to check | Status after the Hard Stop 5 audit |
|---|---|---|---|
| C1. 60 sources logged, 45 included, 15 excluded; included sources by category; 13 of 45 not peer reviewed (Assignment 09, Section 2 and Display 1) | `screening/Screening_Tracker_Full_Scale.xlsx` | Step 2 below rebuilds every number into `counts.txt` | Reproduced exactly from hs5-rc1. After one correction (T#14 is now peer reviewed) the non-peer-reviewed count is 12 |
| C2. A threat-to-control-to-clause chain can be built for 10 sources, and the framework that holds the clause depends on the role of AI (Assignment 09, Display 2) | `mapping/a09_proof_map_links.csv` (one row per link, with quote anchor and link basis), `pilot/hs3-mapping-pilot/03_clause_dictionary.csv` (NIST wording), `04_crosswalk...csv` (NIST crosswalk), `audit/hs5/06_clause_retrace_A6.csv` | Steps 3-4 below; open a row, compare the quote anchor with the clause wording | Downgraded: roles agree (13 of 13) but only 22 of 43 links are anchored in a public abstract and my retrace found 1 of 22 fully supported. Display 2 is a set of candidate links, not evidence |
| C3. The mapping procedure's mechanical steps repeat exactly, but clause links and role codes missed the pilot thresholds (Hard Stop 3) | `pilot/hs3-mapping-pilot/` (pre-registration, coding, three runs, retrace) | `pilot/hs3-mapping-pilot/README.md` | Unchanged |

## 3. Inventory
| Folder or file | What it is | Origin |
|---|---|---|
| `protocol/` | Review protocol (Assignment 1) | Hand-written by me |
| `screening/Screening_Tracker_Full_Scale.xlsx` | All 60 screening decisions with reason, source, query and rank; Progress Summary; Spot-Check Log | Rows 1-12 screened by me; rows 13-60 proposed by Claude under my rule and reviewed by me (audit check A4) |
| `screening/screening-pilot.xlsx` | Smoke Test 2 pilot (5 records) | Assignment 5 |
| `mapping/a09_proof_map_links.csv` | Assignment 09 Display 2 as data: 43 links, each with link basis under Codebook v1.1 and a short quote anchor | Built in Hard Stop 5 from the Assignment 09 memo |
| `analysis/*.py` | Scripts that rebuild counts, check integrity, compare ISO lists, and run the sensitivity check | Written by Claude; reviewed and run as described in `audit/hs5/` |
| `pilot/hs3-mapping-pilot/` | Hard Stop 3 clause-mapping pilot (E01-E17) | See its README |
| `audit/hs5/` | Hard Stop 5 audit: plan (00), review sheets and results (01-03, 06, 08), provenance (04), fresh-run logs and expected outputs (05), discrepancy log (07), audit record (09), feedback response log (10) | This checkpoint; start with `09_audit_record.md` |
| `logs/` | Risk log, known-issues log, changelog | Kept since Assignment 5 |
| `evidence/`, `deliverables/` | Screenshots, the Assignment 09 chart, PDFs of earlier submissions | Earlier checkpoints |

## 4. Provenance
- Searches: Google Scholar (rows 1-12, Oct 2026), targeted web searches (rows 13-24), OpenAlex queries A-D (rows 25-60; query text and rank in the tracker). Dates are in the tracker.
- Clause wording: NIST AI Resource Center (AI RMF Core) and NIST CSF 2.0 Implementation Examples, copied word for word into `03_clause_dictionary.csv`. ISO/IEC 42001 controls come only from NIST's AI RMF-to-ISO/IEC FDIS 42001 crosswalk.
- AI assistance: Claude (Anthropic) proposed screening decisions for rows 13-60, wrote the scripts and summaries, and drafted text. Every use is logged in the AI-use section of each memo. Commit history on GitHub shows the order of work; audit plans were committed before checks were run.

## 5. Prerequisites
Python 3.10 or later with `openpyxl` 3.1 (tested: Python 3.13.16, openpyxl 3.1.5, Linux). Step 1 needs network access once, to install openpyxl; Steps 2-4 need none. Excel or LibreOffice is only needed to read the tracker by eye. On Windows, use `py -m venv .venv` and `.venv\Scripts\activate` in Step 1 and `certutil -hashfile <file> SHA256` instead of `sha256sum` (not tested).

## 6. Steps (run from the repository root)
```
python3 -m venv .venv && . .venv/bin/activate && pip install openpyxl==3.1.5      # Step 1
python3 analysis/rebuild_counts.py screening/Screening_Tracker_Full_Scale.xlsx out   # Step 2: counts.txt, tracker_rows.csv
python3 analysis/check_tracker.py screening/Screening_Tracker_Full_Scale.xlsx out    # Step 3: integrity_report.txt
python3 analysis/compare_a09_iso.py mapping/a09_proof_map_links.csv pilot/hs3-mapping-pilot/04_crosswalk_ai-rmf_to_iso42001.csv pilot/hs3-mapping-pilot/05_annexA_controls.csv out   # Step 4a
python3 analysis/sensitivity.py out/tracker_rows.csv mapping/a09_proof_map_links.csv out   # Step 4b
sha256sum out/*
```
Expected results for this release (hs5-rc2): `counts.txt` reports logged=60, included=45, excluded=15, included_not_peer_reviewed=12; Security controls 12, Security risks 9, AI-related threats 8, Governance 7, Compliance 5, Privacy 2, Human/organizational 2; `integrity_report.txt` reports 0 warnings. Expected SHA-256 values are in `audit/hs5/05_expected_outputs_rc2.txt` (and `05_expected_outputs_rc1.txt` for the audited candidate).

## 7. Restrictions and safe access
- **Abstracts and full texts** are copyrighted and are not stored here. Each source is identified by DOI or OpenAlex ID (`audit/hs5/04_provenance_openalex.csv`), so a reviewer can retrieve the same abstract from OpenAlex or the publisher. Quote anchors are under 15 words.
- **ISO/IEC 42001** is a paid standard and I do not have a copy. ISO matches are provisional and come only from NIST's crosswalk (built on the draft FDIS). The crosswalk files are a substitute that shows the procedure; they do not verify ISO wording.
- **Paywalled sources** (for example Mokgathi & Ogundele 2026; Nolte et al. 2025) were checked on abstract and publisher metadata only.
- **No personal or organizational data** is used. Google Scholar was used only through its normal web interface; when it blocked paging, searching moved to OpenAlex instead of working around the block.

## 8. Known limitations
Single human reviewer with AI support (risk R-02); summaries used in my blind reviews were written by Claude; most sources were read at abstract level, and abstracts rarely support clause-level links (R-09); about a quarter of included sources are not peer reviewed and 15 of 45 are rated low weight (audit/hs5/08); ISO matches are provisional; search results drift over time (R-10); three sources still lack an identifier (T#7, 11, 24). See `audit/hs5/07_discrepancy_log.md`, `logs/risk-log.md` and `logs/know-issues.md`.
