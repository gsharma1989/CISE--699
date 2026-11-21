# Decision rule for clause support (v1.2), fixed 2026-11-20 before any full-text coding

Applies to every proof-map link, full text or abstract, and to both readers. It tightens Codebook v1.1 Step 6.

## Unit
One link = one control named in the source + one framework clause (NIST AI RMF 1.0 subcategory or NIST CSF 2.0 subcategory, wording from the clause dictionary). ISO/IEC 42001 targets are never verdicted: they follow from the NIST crosswalk and stay provisional.

## What counts as an anchor
A quote of 15 words or fewer, with its location (section heading and page or paragraph), describing what the source's own authors do, propose or evaluate. A sentence that only reports other papers (literature review) can make a link Partly at most.

## Verdicts
- **Supported**: the anchor states BOTH the clause's action (for example monitor, detect, analyse, respond, identify, record, evaluate, document, override or deactivate) AND the clause's object (for example networks and network services; vulnerabilities; incidents; the AI system in production; privacy risk of the AI system). Synonyms count ("observe traffic" = monitor networks); implication does not.
- **Partly**: the action OR the object is stated, and the other is only implied, much broader, or much narrower.
- **Not supported**: neither is stated, or the anchor names a threat or an outcome rather than a control.
- **Evidenced gap**: the source shows the clause's control is missing (for example automation "with minimal human intervention" against MANAGE 2.4). Reported separately; not counted as Supported.
- **No full text**: no legal open full text; the abstract-level verdict from Hard Stop 5 stands and is labelled abstract-only.

## Role of AI (fresh coding)
Coded per control from the full text, without looking at the Assignment 09 role: D = AI used by the organization as part of the defence; O = the control protects or governs the organization's own AI; A = the control responds to attackers' AI.

## Worked examples (from records already in release a11-evidence-v1)
| Link | Anchor | Clause | Verdict and why |
|---|---|---|---|
| P13 (T#4) | "continuously monitor network environments, detect anomalies" | CSF DE.CM-01 Networks and network services are monitored | Supported: action (monitor) and object (network environments) both stated |
| P09 (T#3) | "real-time threat detection" | CSF DE.CM-01 | Partly: detection stated; networks not named |
| P01 (T#1) | "explainability and interpretability characteristics of the AI model" | AI RMF MEASURE 2.9 The AI model is explained, validated, and documented | Partly: object (AI model) stated; the actions explain/validate/document are not stated as done |
| P40 (T#52) | "compromise the confidentiality, integrity, and availability of user data" | CSF PR.DS-10 Data-in-use protected | Not supported: names a threat to data, not a protection action |
| P12 (T#4) | "with minimal human intervention" | AI RMF MANAGE 2.4 mechanisms to supersede, disengage or deactivate | Evidenced gap: the override control is shown to be missing |

## Amendment A1 (2026-11-20, during Claude's first pass, before any human verdict)
When a clause names several actions (for example "evaluated and documented"), one stated action applied to the clause's object is enough for Supported; the missing actions are noted in the record.
