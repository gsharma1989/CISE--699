# Clause-Mapping Codebook v1.1

Date: 2026-11-07. Replaces v1.0 after the HS3 pilot. Changes are marked **[v1.1]** with the pilot finding that caused them.

## Step 0 [v1.1]: Snapshot the search first
Save the full ID list of every query at run time (`search_snapshots/<date>_<query>.json`) before screening.
*Why: the OpenAlex re-run on 2026-11-07 changed 10 of 20 logged ranks and added one record (pilot file 07).*

## Step 1: Is the source codable? [v1.1 rule tightened]
Code "Y" only if the text names a **specific technique, tool, process, or organizational practice**, for example "AI-powered SIEM", "continuous monitoring of AI systems", "AI inventory", "manual override". Category words alone ("threat detection", "risk management", "governance frameworks") do **not** count.
If the abstract is generic and an open-access full text exists, read the full text and record that you did. Borderline calls go to the second reader.
*Why: T#33 was codable only on a borderline call, and R1 would have failed (5 of 8) without it.*

## Step 2: Unit of coding [v1.1]
Code **controls, not sources**. A source can give up to 3 control units, chosen by how prominent they are in the text. Each unit gets its own role and links.
*Why: T#25 names more than eight controls; one code per framework lost most of them.*

## Step 3: Role of AI (unchanged)
D = defence tool; O = own AI at risk or governed; A = attacker's tool. Note a second role if present.

## Step 4: Clause links [v1.1 link basis]
- Choose clauses only from the clause dictionary.
- Every link must be labelled:
  - **evidenced**: there is a quote anchor in the source for this link; or
  - **rule-inferred**: the link follows from the role rule (for example, a D-role tool's own monitoring under MEASURE 2.4) but the source says nothing about it.
- Only evidenced links count as traceability evidence. Rule-inferred links are reported separately.
- If nothing fits: `NONE` (FR6 unresolved).
*Why: v1.0 told the coder to pick a tool-trust AI RMF clause for D-role sources and also required an anchor. For T#9 and T#33 these conflicted. A check of Assignment 09 found 4 of its 6 D-role rows rested on a rule-inferred AI RMF link (pilot file 13).*

## Step 5: Clause dictionary changes [v1.1]
Add a clause only by copying it word for word from NIST's own page, with the date, in `03_clause_dictionary_changelog.md`. First additions: RS.MI-01 and RS.MI-02 (incident containment and eradication), to be copied from the NIST CSF 2.0 page.
*Why: T#40 asks for containing breach spread; with no containment clause in the dictionary, it was forced to the nearest recovery clause (RC.RP-01, retrace = Partly).*

## Step 6: Evidence and retrace (unchanged, plus second reader)
Quote anchor under 15 words; confidence H/M/L; retrace each link as Supported / Partly / Not supported. **[v1.1]** A second reader (the student) codes role and codability blind for every unit in a 25% sample; agreement is reported.
