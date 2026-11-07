# Review sheet sent to me for checks A4 and A5 (2026-11-07)

Prepared by Claude from the tracker and the Assignment 09 proof map. The recorded decisions and roles were not shown. I answered from these summaries without opening the tracker or the Assignment 09 memo. Answers were given in the chat at about 18:10 UTC and are recorded in 02_screening_review_A4.csv and 03_role_coding_A5.csv.

## A4 rule given to me
Include if the source is substantively about AI and cybersecurity risk (threats, controls or governance). Exclude if (a) it is not really about cybersecurity or not really about AI; (b) it collects primary data from a real organisation; (c) it is mainly about building or training a specific ML algorithm; (d) it gives operational attack detail; (e) there is not enough information to judge it.

## A4 summaries (38 rows: 13, 14, 16-22, 24-28, 31-34, 36-39, 43-51, 53-56, 58-60)
| Row | Summary shown to me |
|-----|---------------------|
| 13 | Review of adversarial ML methods and tools in four critical sectors (evasion, poisoning, privacy leakage), linked to EU AI Act robustness duties; also has sections on defence algorithms |
| 14 | Preprint survey of AI-enabled threats (deepfakes, adversarial attacks, AI malware, AI phishing) and defences (adversarial training, EDR/XDR, human review) |
| 16 | Legal analysis of EU AI Act robustness and cybersecurity duties for high-risk and general-purpose AI |
| 17 | Preprint mapping EU AI Act requirements to verification activities based on ISO/IEC 42001, with an automotive intrusion-detection case |
| 18 | Intrusion-detection design that maps policy rules to NIST AI RMF functions and logs every decision; tested on a public dataset |
| 19 | Practitioner article on cyber risk governance for AI (NIST AI RMF, ISO/IEC 42001, FAIR-AIR; board accountability) |
| 20 | PRISMA review of 36 studies plus an audit model; argues audit should move from periodic checks to continuous risk governance |
| 21 | Journal article on AI-enabled attacks, AI defences and governing dual-use AI (NIST AI RMF, EU AI Act) |
| 22 | Review of 236 studies sorting AI security uses by NIST CSF functions |
| 24 | Systematic review of how GAN-based defence models are built and trained (architectures, training, metrics) |
| 25 | Book on moving from rule-based to predictive AI cybersecurity controls |
| 26 | AI for continuous cybersecurity audit and risk management |
| 27 | Literature review of AI tools for threat detection, response and risk management |
| 28 | AI for cybersecurity risk management in IoT systems |
| 31 | Paper building an AI fraud-detection model for digital finance |
| 32 | Integrated risk management in hospitals (patient safety, clinical risk); information security is one item in a list |
| 33 | AI for detecting ransomware, phishing and DDoS and automating response |
| 34 | Literature review and framework for AI decision-support systems in cybersecurity, including governance |
| 36 | Case study at a named bank on AI and operational banking risk |
| 37 | Analysis of a public database of AI security incidents (attack types, targeted AI parts, CVSS/EPSS scores) |
| 38 | AI in financial (credit and market) risk management |
| 39 | Technological and socio-political risks of AI in cybersecurity (cases like the Tay chatbot) |
| 43 | Record with no abstract, only a citation. Title: "AI-based dynamic risk management models in cybersecurity: real-time monitoring and decision making" |
| 44 | Compares NIST AI RMF, MITRE ATLAS, ENISA, ISO/IEC 42001 and AI-SEC frameworks on six dimensions |
| 45 | AI governance for data privacy compliance and cybersecurity risk in companies |
| 46 | AI for disaster risk management in the beauty industry; cybersecurity is one item among supply chain and crisis response |
| 47 | How AI changes cybersecurity and digital governance policy |
| 48 | Governance challenges from adversarial attacks on AI systems |
| 49 | Preprint position paper: AI risk management must treat AI safety and security together |
| 50 | Whether enterprise cyber risk management can cope with AI-driven attacks |
| 51 | Layered risk-and-controls framework for prompt injection in company AI tools |
| 53 | Framework for bringing AI workloads (prompt injection, drift, poisoning) into enterprise risk management in the cloud |
| 54 | AI tools for information security risk management, and the new risks they bring |
| 55 | Conference abstract linking NIST AI RMF functions to a risk taxonomy and 25 control domains |
| 56 | Lifecycle risk, robustness and regulatory compliance for AI in fintech, including cybersecurity |
| 58 | Paper building RNN/LSTM models to detect insider threats |
| 59 | Insider-threat risk management in cyber and cyberbiosecurity; AI appears only as one industry where insiders work |
| 60 | Synthesis of AI approaches to insider-threat detection (behaviour analytics, NLP, LLMs, graphs) and their limits |

## A5 rule given to me (Codebook v1.1, Step 3)
Whose AI is it, and what is the control doing? D = the organisation uses AI as part of the control to protect its systems; O = the control protects or governs an AI system the organisation owns or runs (protecting ordinary IT systems is not O); A = the control responds to attackers using AI.

## A5 items (Assignment 09 Display 2, 13 rows)
Item to tracker row: B1 T#1, B2 T#2, B3 T#3, B4 T#4, B5 T#5, B6 T#18, B7 T#8, B8 T#6, B9 T#17, B10 T#52, B11 T#14, B12 T#21, B13 T#50 (the row numbers were not shown to me).

| Item | Threat -> control shown to me |
|------|------------------------------|
| B1 | Exploitable vulnerabilities -> an AI model ranks the organisation's vulnerabilities and explains each ranking |
| B2 | Ransomware on critical infrastructure -> AI anomaly detection and response |
| B3 | Threats to IT projects -> AI risk prediction, real-time detection, automated response |
| B4 | Evolving threats -> machine-learning monitoring and response "with minimal human intervention" |
| B5 | Large-scale threats -> AI detection, faster response and recovery |
| B6 | Network intrusions -> an intrusion-detection system whose AI decisions are checked against policy and logged |
| B7 | Staff using unapproved AI tools -> AI use policy, AI inventory, staff training |
| B8 | Privacy risks from AI datasets, models and human error -> privacy risk assessment including human factors |
| B9 | EU AI Act duties for a high-risk AI system -> manual override, drift detection, model cards |
| B10 | Evasion, poisoning and inversion attacks on AI models -> adversarial training, differential privacy, smoothing |
| B11 | AI-made phishing, deepfakes and AI malware -> detection tools, staff training, human review |
| B12 | AI-enabled attacks on organisations -> AI defences plus governance of dual-use AI |
| B13 | AI- and ML-driven adversarial attacks on enterprises -> enterprise cyber risk management practice |

Limits on independence: the summaries were written by Claude, who also proposed the recorded decisions and roles; I wrote and submitted Assignment 09 on 2026-10-29, so I may remember some roles. This is a blind second reading, not independent replication.
