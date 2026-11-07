# Recorded walkthrough: script and click path (about 8-9 minutes)

How to record on Windows 11: open the Snipping Tool, choose **Record**, select the browser window, click **Start**. (Or Xbox Game Bar: Win + Alt + R.) Speak slowly; it is fine to read this script. Upload the video to Canvas (media recording or file upload).

Before recording, open these tabs:
1. https://github.com/gsharma1989/CISE--699/releases
2. https://github.com/gsharma1989/CISE--699/tree/hs5-rc2
3. The memo PDF (HardStop5_Audit_Memo.pdf)

---

**1. Introduction (0:00-0:45)** - Tab 1 (Releases)
"Hi, I am Gaurav Sharma. This is my Hard Stop 5 walkthrough for my thesis on AI-driven cybersecurity risk management. I will show what is in my research package, how I audited it, what went wrong, and how a reviewer can check my main claims. Everything is in my GitHub repository. This page shows the frozen releases: hs5-rc1 is the release candidate I audited, and hs5-rc2 is the corrected version I am submitting."

**2. The package and the README (0:45-2:00)** - Tab 2, scroll the README
"The README is the map. Section 2 lists my three principal claims, the records behind each one, how to check it, and its status after the audit. Section 3 is the inventory: the screening tracker, the mapping data, the analysis scripts, the Hard Stop 3 pilot, the audit folder, and my logs. Section 7 explains what is restricted: abstracts are copyrighted, so I store only their OpenAlex IDs and DOIs, and ISO/IEC 42001 is a paid standard, so ISO links come only from NIST's crosswalk and stay provisional."

**3. The audit plan came first (2:00-2:45)** - open audit/hs5/00_audit_plan.md, then click History
"Before running any check I committed this audit plan. It sets eight checks and a pass mark for each. The commit history shows it was saved before the results."

**4. Audit results (2:45-3:45)** - open audit/hs5/09_audit_record.md
"This table is the audit record. The fresh run passed: two clean folders, the README steps only, and every output matched the expected hash. My blind review of the 38 screening decisions I had not checked agreed 38 out of 38. My role coding agreed 13 out of 13. But the clause-link check failed: when I retraced 22 links, I found only 1 fully supported. I will come back to that."

**5. Claim-to-record path, claim C1 (3:45-4:45)** - open audit/hs5/05_fresh_run_log_rc1.txt, then the memo table
"Here is how a reviewer checks my first claim, that 45 of 60 sources were included. The README Step 2 command rebuilds every number from the tracker into counts.txt. This log shows the fresh run: files downloaded from the tag, a new Python environment, both runs identical, and the numbers match what Assignment 09 reported."

**6. Claim-to-record path, claim C2 (4:45-6:15)** - open mapping/a09_proof_map_links.csv, find row P13, then pilot/hs3-mapping-pilot/03_clause_dictionary.csv, then audit/hs5/06_clause_retrace_A6.csv
"My second claim is the proof map from Assignment 09. Each link is now one row. Row P13 is Femi and Medugu: the quote from the abstract is 'continuously monitor network environments, detect anomalies', linked to NIST CSF DE.CM-01. In the clause dictionary, DE.CM-01 says 'Networks and network services are monitored to find potentially adverse events'. The quote states that action, so I marked it Supported. Now row P01, Islam and others: the quote is about explaining the AI model, linked to MEASURE 2.9, which also requires the model to be validated and documented. Claude marked it Supported, but I marked it Partly, because the quote only covers part of the rule. Most links were like this: only 1 of 22 fully supported in my retrace. So my conclusion is that Display 2 is a set of candidate links, not evidence, until I code the full texts."

**7. Discrepancies and fixes (6:15-7:30)** - open audit/hs5/07_discrepancy_log.md
"The audit found nine discrepancies. Three examples. D1: the tracker IDs were formulas, so sorting the sheet would change every citation; I froze them as numbers. D3: one source I had marked as a preprint is now published in a peer-reviewed Springer proceedings; I corrected it, so non-peer-reviewed sources go from 13 to 12. D8: my README said no internet was needed, but installing the Python library needs it; I fixed the README. Each fix is in hs5-rc2, and the remaining open items are listed in the last column."

**8. AI use and independence (7:30-8:30)** - memo, AI log section
"I used Claude as a research assistant. It wrote the scripts and the neutral summaries, proposed the earlier screening decisions, and did the first-pass coding. I made every verdict in the four review checks myself, without seeing the recorded answers. This is a self-audit with a blind second reader, not independent replication, because the summaries I read were written by the AI and I wrote Assignment 09 myself."

**9. What happens next (8:30-9:00)**
"For Assignment 11, I will cite the hs5-rc2 release, code the open-access full texts for the proof-map sources, write a clear rule for when a link counts as supported, and report the role-of-AI pattern only as a hypothesis until those links hold. Thank you."
