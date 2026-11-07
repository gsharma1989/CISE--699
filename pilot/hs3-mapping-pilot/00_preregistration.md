# HS3 Pilot Pre-Registration: Clause-Mapping Procedure Trial

Project: AI-Driven Cybersecurity Risk Management (CISE 699 thesis, Gaurav Sharma)
Written: 2026-11-07, before any pilot coding was done. Committed to GitHub before execution so the order can be checked.
Procedure version: Clause-Mapping Codebook v1.0 (file `01_codebook_v1.0.md`)

## Assumption under test

The highest-risk step in my design is Control Selection → Governance & Compliance Obligation (Assignment 04, Section 6.2). The procedural assumption behind it is:

> Following a written procedure, a control described in a source's public abstract or publisher page can be (a) given one role of AI and (b) linked to a specific NIST AI RMF 1.0 subcategory and NIST CSF 2.0 subcategory (plus an ISO/IEC 42001 control through the NIST crosswalk), and each link can be traced back to the source text and the clause wording, and repeated with the same result.

## Sample (fixed before coding)

- Frame: the 32 included sources in `screening/Screening_Tracker_Full_Scale.xlsx` that were **not** clause-mapped in Assignment 09.
- Draw: 8 sources, Python `random.Random(20261107).sample(...)`, script `02_draw_sample.py`.
- Drawn rows: T#9, T#16, T#25, T#33, T#40, T#47, T#48, T#49.
- Inputs allowed: public abstracts (OpenAlex record or publisher/arXiv page) only. No paywalled full text. ISO/IEC 42001 itself is not available to me (paid), so ISO matches come only from the NIST crosswalk and are labelled provisional.

## Readiness criteria (set before execution)

| ID | Check | Usable if | Needs revision if |
|----|-------|-----------|-------------------|
| R1 | Codability: control described specifically enough to code from public text | ≥ 6 of 8 sources | < 6 of 8 |
| R2 | Traceability: every link has a source quote anchor and a clause ID from the dictionary; self-retrace finds the clause wording supports the link | ≥ 80% of links supported | < 80% supported, or any link without an anchor |
| R3 | Repeatability: crosswalk lookup script run twice on the same input | Byte-identical outputs (SHA-256 match) | Any difference |
| R4 | Role agreement: my blind role codes vs the AI-proposed role codes | ≥ 7 of 8 agree | ≤ 6 of 8 agree |
| R5 | Search input stability: re-run of OpenAlex Query A (logged 2026-10-29) | Logged top-20 records still returned; rank changes explained | Logged records missing without explanation |

A failed criterion is a result, not a reason to drop the pilot. Any failure will be reported with a diagnosis and a protocol change.
