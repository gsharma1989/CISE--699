# HS3 Pilot: Clause-Mapping Procedure Trial (2026-11-07)

This folder holds the full record of the Hard Stop 3 (thesis format) pilot. It tests whether my clause-mapping procedure can link a control in a source to a named NIST AI RMF 1.0 / NIST CSF 2.0 clause (and an ISO/IEC 42001 control via the NIST crosswalk) in a way that can be traced and repeated.

## Order of work (check the commit times)
1. `00_preregistration.md`, then `01`–`05` were committed **before** any coding (commits 3c81870 and 8f38b6a, 2026-11-07 02:49 and 02:51 UTC).
2. Inputs were checked (`06`, `07`), then the sample was coded (`08`), the lookup was run three times (`09`, `10`, `run1`–`run3`), the validator was tested with seeded errors (`11`), each link was retraced (`12`), and Assignment 09 was re-checked against the same rule (`13`).
3. The procedure was revised to v1.1 (`14`). Role coding by me (`15`) is the second-reader check.

## How to repeat the computational steps
Environment used: Ubuntu 24.04.5, Python 3.13.16, openpyxl; no network needed for steps 1–2.
```
python3 02_draw_sample.py ../../screening/Screening_Tracker_Full_Scale.xlsx   # sample=9,16,25,33,40,47,48,49
python3 09_map_lookup.py 08_coding_passA.csv 03_clause_dictionary.csv 04_crosswalk_ai-rmf_to_iso42001.csv 05_annexA_controls.csv runX
sha256sum runX/*   # should match run1/ (see 10_run_log.txt)
```
The search re-run (`07`) needs internet access to the OpenAlex API; its query string is in `07_search_rerun_comparison.csv` notes and in the memo. Results can drift because the index changes (see `07`).

## What is not in this folder, and why
- Full abstracts are not copied here (copyright). `06_input_check.csv` keeps each record's OpenAlex ID, DOI, retrieval time, length, and a SHA-256 fingerprint so the same text can be re-fetched and checked.
- ISO/IEC 42001 text is paid and not available to me. ISO matches come only from NIST's crosswalk (built on the draft FDIS) and are provisional.

## File index
| ID | File | What it is |
|----|------|-----------|
| E01 | 00_preregistration.md | Assumption, sample, readiness criteria R1–R5 (written before coding) |
| E02 | 01_codebook_v1.0.md | Procedure version used in the pilot |
| E03 | 02_draw_sample.py, 02_draw_sample_output.txt | Random sample draw (seed 20261107) |
| E04 | 03_clause_dictionary.csv | 19 AI RMF + 25 CSF 2.0 clauses, wording copied from NIST pages |
| E05 | 04_crosswalk_ai-rmf_to_iso42001.csv, 05_annexA_controls.csv | NIST crosswalk targets; Annex A control list (38) |
| E06 | 06_input_check.csv | Input availability, type, peer-review status, fingerprints |
| E07 | 07_search_rerun_comparison.csv | OpenAlex Query A re-run vs logged ranks |
| E08 | 08_coding_passA.csv | Coding records (Pass A) |
| E09 | 09_map_lookup.py | Lookup and validation script |
| E10 | 10_run_log.txt, run1/, run2/, run3/ | Three runs, SHA-256 hashes, identical |
| E11 | 11_control_test_input.csv, 11_control_test_result.txt | Validator positive control: two seeded errors, both caught |
| E12 | 12_retrace_audit.csv | Link-by-link retrace (self-check, not independent) |
| E13 | 13_a09_retrospective_check.csv | Assignment 09 D-role links re-checked against the same rule |
| E14 | 14_codebook_v1.1.md | Revised procedure |
| E15 | 15_role_coding_check.md | My blind role coding vs Pass A (R4) |
