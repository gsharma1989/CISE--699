# 12 Re-test of the role-of-AI pattern (A12)

Responds to: A11 feedback, contribution. The role-of-AI pattern is tentative: it may reflect framework scope or coding rules. Re-test it independently of the original mapping. A documented negative result is acceptable.

## Pattern under test (A11, Section 4.4.4)

The role of AI predicts which framework holds the clause:

- **Defence-tool AI (D):** operational clause in NIST CSF 2.0; AI RMF covers only the tool's trustworthiness.
- **Organization's own AI (O):** direct AI RMF / ISO/IEC 42001 clauses.
- **Attacker AI (A):** no AI RMF clause.

**Refutation test (fixed in A11):** the pattern fails if

- a control coded D has a Supported AI RMF link, or
- a control coded O has no AI-framework link.

## How the re-test is independent of the original mapping

1. **Role coded per control from the full text, not per source from the abstract.** Under rule v1.2, Claude coded roles without looking at the A09 role. Gaurav reviewed the codes and agreed; this was not blind.
2. **Only full-text verdicts under the fixed rule v1.2 count.**
3. **A second human reader coded roles on a fresh sample of 8 sources** that were never mapped (05_*).
4. **Script:** `analysis/role_retest.py`. **Output:** `12_role_retest_output.txt`.

**Limits of independence:**

- The clauses tested are still the 43 links that the original map proposed.
- The A12 first-pass coder (Claude) also took part in the original mapping.

## Results

**Role changes**

- 5 of 41 coded links change role when coded per control.
- Four go D → O:
  - T#2: security evaluation of the AI model.
  - T#18: policy, monitoring and logging that govern the IDS's own AI.
- One goes A → O:
  - T#14: the paper's own controls protect the organization's AI.

**The "A" group dissolves in the full texts**

- The attacker-side sources' own controls are D or O.
- Only one A-coded link remains, P42, and it is abstract-only.

**At control level (full text)**

- **D controls:**
  - AI RMF: 0 Supported (1 Not supported, 1 evidenced gap).
  - CSF: 1 Supported, 5 Partly.
- **O controls:**
  - AI RMF: 4 Supported, 4 Partly, 1 Not supported.
  - CSF: 1 Supported, 5 Partly, 3 Not supported.
- **Refutation check 1** (D control with a Supported AI RMF link): none.
- **Refutation check 2** (O controls with no AI RMF link): T#14. Its O-coded control (adversarial training) was never offered an AI RMF clause, because the A09 map gave attacker-side sources none.
  - This is an artefact of the original mapping rule.
  - The pattern "A sources have no AI RMF clause" was produced by the coding rule, not found in the literature.

**Second reader, fresh sample:**

- Role agreement 4 of 6, kappa 0.43. The target was 7 of 8, so it was not met.
- The two disagreements are D vs O (T#37) and A vs O (T#44). These are exactly the boundaries the pattern depends on.

## Verdict (documented negative result)

- **As a finding about the literature, the source-level role pattern is not supported.**
  - Roles change when coded per control.
  - The attacker-side group disappears in the full texts.
  - One leg of the pattern was created by the mapping rule.
  - Two human readers do not yet agree on roles at the needed level.
- **What survives is a consequence of framework scope, not an empirical regularity.**
  - At control level, controls that govern an AI system as an asset (O) find AI RMF clauses.
  - Controls that use AI to defend networks (D) find CSF clauses.
  - This follows from how O is defined and from the AI RMF's scope (AI systems the organization designs, develops, deploys or uses).
- **Thesis change:**
  - The role pattern moves from "provisional hypothesis" to "not supported as a finding; kept as a mapping heuristic derived from framework scope". The heuristic is: classify each control, not each source, by what it protects.
  - Conclusion 1 is unaffected.
