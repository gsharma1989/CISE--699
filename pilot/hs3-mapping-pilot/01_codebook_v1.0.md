# Clause-Mapping Codebook v1.0

Used for: Control Selection → Governance & Compliance Obligation (Assignment 04, Sections 2.3 and 6.2).
Date: 2026-11-07. Supersedes the informal function-level mapping used at Hard Stop 4.

## Step 1: Is the source codable?
Read the public abstract (or publisher page). Code "Y" only if it names at least one **concrete control or practice** (something an organization does), not just "AI improves security". Otherwise code "N" and stop (record reason).

## Step 2: Role of AI (pick one)
- **D = Defence tool**: the control is itself an AI system used to protect (detection, response, risk scoring).
- **O = Own AI at risk / governed**: the organization's own AI system or AI use is the thing that is attacked, leaks, is misused, or must be governed.
- **A = Attacker's tool**: the threat is AI used by an attacker against the organization.
- If two roles apply, code the role of the **main control** and note the second role.

## Step 3: Clause links
- Choose the closest **NIST AI RMF 1.0** subcategory and the closest **NIST CSF 2.0** subcategory, **only from the clause dictionary** (`03_clause_dictionary.csv`), whose wording was copied from NIST's own pages.
- Rule for role D: the AI RMF clause covers the tool's own trustworthiness (monitoring, explanation, security); the CSF clause covers what the tool does.
- Rule for role A: no AI RMF clause (the AI RMF covers an organization's own AI). CSF only.
- If nothing in the dictionary fits, write `NONE` (this is an FR6 "unresolved" flag, not a failure).
- ISO/IEC 42001 is **not** coded by hand. The lookup script fills it from the NIST crosswalk (`04_crosswalk_ai-rmf_to_iso42001.csv`), converting Annex B numbers to the matching Annex A control.

## Step 4: Evidence for each link
- `quote_anchor`: a short phrase (under 15 words) from the source showing the control.
- `confidence`: H (control and clause clearly match), M (reasonable but another clause could fit), L (weak fit).

## Step 5: Retrace
For each link, a second pass checks: anchor present; clause ID exists; clause wording supports the link (Supported / Partly / Not supported), with a one-line reason.
