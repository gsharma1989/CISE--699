# 08 MITRE ATLAS update round (R4): snapshot, screening and chain check

Responds to: A11 feedback Priority 3 ("screen MITRE ATLAS within the source limit and explain how new sources change conclusions").
Prepared by Claude on 2026-11-20. Screening decisions were **proposed** by Claude; Gaurav reviewed all 20 on 2026-11-20 and agreed (not blind; column `author_review` in `08_atlas_screening.csv`, and `08_atlas_author_review_NOTE.md`). He then reviewed the tiers and changed three (rows 61, 65, 79); see the author review note.

## 1. Query and snapshot

- Query E, OpenAlex: `search="MITRE ATLAS"`, publication dates 2023-01-01 to 2026-12-31, `has_abstract:true`, 50 per page.
- Retrieved 2026-11-20T17:07:51Z in the browser pane. OpenAlex reported **608** records.
- Ranks 1-50 are saved in `08_atlas_snapshot.csv` (ID, DOI, year, type, title, venue, first authors). Abstracts are not stored in the record.
- **Drift note:** The thesis draft (A11, Section 3.4) reported 151 records for a MITRE ATLAS query. That query string was not saved, so it cannot be compared with this one. From now on, the saved snapshot file is the reference.

## 2. Screening within the 80-source cap

- The protocol caps the corpus at 80 logged sources. Rows 1-60 were already used, so ranks 1-20 were screened as tracker rows 61-80 (round R4). Ranks 21-50 were saved but not screened.
- **Result:** 20 screened; **11 included** (rows 61, 63, 64, 65, 68, 70, 71, 74, 78, 79, 80) and 9 excluded.
- **Reasons for exclusion:**
  - Tool or low-level engineering: 2, 6, 7, 9.
  - Attack modelling below category level: 13, 16.
  - Not English: 12.
  - Duplicates: 15 duplicates 8, and 17 duplicates 11.
- **Peer-review flag:** 5 of the 11 includes are not peer reviewed (preprint or repository: rows 68, 70, 71, 74, 80). Three more have peer review unclear (rows 61, 78, 79).
- **Tiers:** proposed by Claude as 1 / 1 / 9; after Gaurav's review, Tier 1: 2 (rows 64, 79), Tier 2: 3 (rows 61, 63, 65), Tier 3: 6.
- **Counts after R4** (`out/counts.txt`): logged 80, included 56, excluded 24, not peer reviewed 17.
- The 11 R4 sources are used **only** to test the search-bias alternative and the gap claim. They were not added to the proof map, the role coding or the Display 5 counts, which stay on the 45 sources of Rounds 1-3. This follows the PRISMA 2020 pattern for an update round: previous studies plus new studies, reported separately.

## 3. Chain check on the sources most likely to break the gap claim

**Test:** does the source trace a named AI threat, through a control, to a **numbered** clause in a governance framework, with evidence for each link?

| Row | Source | What was read | Threat → control | Numbered clauses | Evidence per link | Peer reviewed |
|---|---|---|---|---|---|---|
| 71 | Adversarial RL (2026), AI Compliance & Security Matrix | Zenodo record and abstract. The PDF was binary and could not be read; the CSV was blocked. | Claimed | EU AI Act "Article 15" is named; ISO/IEC 42001:2023 is named without control numbers in the readable text | Not visible; claims "a definitive, verifiable normative mapping" | No. Repository record, anonymous author, no method |
| 68 | Ayada (2026), DARR risk register | Zenodo record only. The GitHub repository was blocked. | Risks → frameworks; no control layer visible | None visible (only standard numbers) | Not shown; "cross-checked" with no method | No. Repository software record |
| 70 | Ee et al. (2024), defense-in-depth | Full text, 80 pp. (arXiv PDF read in the browser pane) | Framework-level comparison | AI RMF subcategories cited only as examples ("Manage 4.1"). No ATLAS technique linked to a numbered clause. No CSF subcategory IDs found by pattern search | Not applicable | No. Think-tank report on arXiv |
| 65 | Carroll (2025), ECCWS | Full text (PDF as text) | Threat → ATLAS mitigation (one worked example) | None | Single example; no mapping method | Conference; statement not seen |
| 74 | Johnson (2026), evaluation-deployment gap | Abstract | Argues ATLAS and AI RMF leave a runtime gap | Not in the abstract | Not applicable | No. Preprint |

**Result:** none of the five passes the test.

- Two non-peer-reviewed repository artefacts from 2026 (rows 68 and 71) **claim** threat-to-framework mappings, including ISO/IEC 42001 and the EU AI Act. Their mapping files could not be read, and neither reports a method.
- Ee et al. (2024) explicitly calls for this work. It recommends building "comprehensive databases of TTPs and mitigations" and expanding ATLAS. This supports the gap claim: the gap is named as open in the literature itself.

## 4. How the new sources change the conclusions

1. **Conclusion 1 (threats and controls are described, effectiveness and exact clause links are not proven): unchanged, slightly strengthened.**
   - Four sources add threat synthesis: two peer-reviewed journal reviews (rows 63, 64) and two with peer review unclear (rows 61, 79).
   - Three add controls in ATLAS terms (rows 65, 78, 80).
   - None measures whether a control works.
2. **The gap claim must be narrowed.** The A11 claim was that no source in the corpus builds the full chain. It now reads:
   > No peer-reviewed source in the 56 included sources traces an AI threat through a control to a numbered framework clause with evidence for each link. Two 2026 repository artefacts claim such mappings, but they are not peer reviewed, report no method, and their mapping tables could not be read.

   These two artefacts are reported as **unverified possible counter-evidence**, not ignored.
3. **The search-bias alternative (Section 5.2) is partly supported.**
   - A threat-framework query finds mapping attempts that the governance query string missed.
   - Those attempts sit in grey literature, outside peer review.
   - So the gap is a gap in **peer-reviewed, evidenced** mapping. It is not a gap in attempts.
4. **The role-of-AI pattern** is not tested by R4, because the R4 sources were not role-coded. See `12_role_retest.md`.

## 5. Limits of this round

- Only ranks 1-20 of 608 were screened, because of the 80-source cap.
- Rows 68 and 71 could not be read in full.
- Screening decisions were proposed by Claude from abstracts and records, and need Gaurav's review.
- OpenAlex relevance ranks drift over time; the snapshot file fixes what was seen on 2026-11-20.
