# R4: Blind Role Coding (second reader)

Status: **done** on 2026-11-07 (my codes given at 03:19 UTC). I coded the role of AI for each of the 8 sample sources from a one-line neutral summary, without seeing Pass A. The summaries were written by Claude, so this check is not fully independent: a summary can steer the reading (see T#25).

Roles: D = AI as defence tool; O = the organization's own AI is at risk or governed; A = AI as the attacker's tool.

| Row | Neutral summary | My code | Pass A (main; second) | Agree (main role) |
|-----|-----------------|---------|-----------------------|-------------------|
| T#9 | Review of AI for intrusion detection, malware classification, and network anomaly detection in organizations | D | D | Yes |
| T#16 | Legal analysis of EU AI Act duties that high-risk AI systems be robust and secure | O | O | Yes |
| T#25 | Book on AI in SIEM, intrusion detection, incident triage, identity management; also covers attacks on AI and AI-made phishing | A | D; O, A | No (my code is a Pass A second role) |
| T#33 | Chapter on AI improving threat detection and response automation against ransomware, phishing, DDoS | D | D | Yes |
| T#40 | IMF note: AI speeds up finding and exploiting weaknesses; harm spreads through shared providers; calls for containment and recovery | O | A; O | No (my code is a Pass A second role) |
| T#47 | Article on how AI changes national and institutional cybersecurity policy, including AI-enabled attacks | O | D; A | No |
| T#48 | Paper on governance of adversarial attacks on AI systems: oversight, training, continuous monitoring | O | O | Yes |
| T#49 | Position paper: AI risk management must treat AI safety and AI security together | D | O | No |

## Result
- Main-role agreement: **4 of 8 (50%)**. Pre-registered criterion R4: usable if at least 7 of 8 agree. **R4 fails.**
- Cohen's kappa = 0.18 (observed 0.50, chance 0.39): only slight agreement beyond chance.
- Sensitivity check (not pre-registered): counting my code as agreeing when it matches a Pass A second role gives 6 of 8, which still fails.
- Codable sources only (R1 = Y): 4 of 6 agree. Both non-codable sources (T#47, T#49) disagree; a role is hard to fix when the source names no control.

## Why we disagreed
1. Mixed-role sources (T#25): the book covers all three roles, and a single role per source forced a choice. The summary's last clause ("attacks on AI and AI-made phishing") may have pulled my reading toward A.
2. "O" read two ways (T#40, T#47): I used O for "the organization's systems need protecting"; Pass A uses O only when the organization's own AI is the thing at risk or governed.
3. No named control (T#47, T#49): with no control to anchor on, the role became a judgment about the whole paper.

## What changes
Codebook v1.1 Step 3 now codes the role per control unit with a decision question and tie-break rules, gives no role to non-codable sources, and requires R4 to be re-tested on a fresh sample before any role-of-AI pattern is reported.
