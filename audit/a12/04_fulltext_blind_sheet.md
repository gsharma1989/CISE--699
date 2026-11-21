# Blind sheet: full-text link check (for Gaurav)

Fill in the last column for every row: **S** (Supported), **P** (Partly), **N** (Not supported) or **G** (gap: the source shows the control is missing). Use the rule below. Do not look at any earlier verdicts.

**Rule:** S = the quote states BOTH the clause's action (for example monitor, analyse, evaluate, document, override) AND what it acts on (for example networks, the AI model, personnel). One action is enough if the clause lists several. P = only one of the two is stated, or the quote only reports other people's work. N = neither, or the quote names a threat or a risk instead of a control. G = the source shows the control is missing.

| # | Framework rule (NIST wording) | Quote from the source | Where | Whose words | Your verdict (S/P/N/G) |
|---|---|---|---|---|---|
| 1 | DE.CM-09: Computing hardware and software, runtime environments, and their data are monitored to find potentially adverse events | "detailed, tamper-evident logs of system operations are maintained and reviewed" | Sec. 3.7, R7.2 table (M7.2) | Authors' own |  |
| 2 | DE.CM-01: Networks and network services are monitored to find potentially adverse events | "Detection involves the prompt monitoring and identification of cybersecurity events or anomalies" | Sec. 2.1 Simple Cyber Threats | Reports other work or describes a risk/incident |  |
| 3 | RS.MA-01: The incident response plan is executed in coordination with relevant third parties once an incident is declared | "Colonial's IT and security teams collaborated with federal agencies such as the FBI" | Sec. 3.2 | Reports other work or describes a risk/incident |  |
| 4 | MEASURE 2.10: Privacy risk of the AI system - as identified in the map function - is examined and documented. | "help organisations systematically assess AI privacy risks" | Sec. 6 Conclusion | Authors' own |  |
| 5 | MANAGE 2.4: Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use. | "with minimal human intervention" | Abstract p.106; Future Directions p.109 | Authors' own |  |
| 6 | RS.MA-01: The incident response plan is executed in coordination with relevant third parties once an incident is declared | "AI can automate incident response processes" | Abstract p.106 | Authors' own |  |
| 7 | MEASURE 2.4: The functionality and behavior of the AI system and its components - as identified in the map function - are monitored when in production. | "The audit process operates continuously as part of the inference pipeline." | Sec. 4.6 | Authors' own |  |
| 8 | DE.AE-02: Potentially adverse events are analyzed to better understand associated activities | "AI systems were able to analyze large volumes of transactional data" | Results, Case Studies p.109 | Reports other work or describes a risk/incident |  |
| 9 | MEASURE 2.9: The AI model is explained, validated, and documented, and AI system output is interpreted within its context - as identified in the map function - to inform responsible use and governance. | "All models used are accompanied by documentation on training data, assumptions, and risks" | Sec. 4, Table 12 (T4.2) | Authors' own |  |
| 10 | PR.AT-01: Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with security risks in mind | "human-centred privacy controls require commensurate attention as technical measures" | Sec. 4.5 | Authors' own |  |
| 11 | GV.PO-01: Policy for managing cybersecurity risks is established based on organizational context, cybersecurity strategy, and priorities and is communicated and enforced | "requires the implementation of comprehensive AI governance systems encompassing risk management procedures" | Sec. 5, p.604 | Authors' own |  |
| 12 | GOVERN 1.2: The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices. | "organisations should aim to build comprehensive AI governance systems encompassing security policies" | Sec. 4, p.603 | Authors' own |  |
| 13 | ID.RA-03: Internal and external threats to the organization are identified and recorded | "Identify and block adversarial inputs or escalate them for human review" | Sec. 3.3 (cited [16]) | Reports other work or describes a risk/incident |  |
| 14 | PR.AT-01: Personnel are provided with awareness and training so that they possess the knowledge and skills to perform general tasks with security risks in mind | "It is also crucial to develop employees' digital skills" | Sec. 4, p.603 | Authors' own |  |
| 15 | ID.RA-03: Internal and external threats to the organization are identified and recorded | "Cyber threat actors are leveraging AI and ML techniques" | p.73, Efficacy of current practices | Authors' own |  |
| 16 | MEASURE 2.7: AI system security and resilience - as identified in the map function - are evaluated and documented. | "continuous validation, model integrity testing, and red-teaming of AI-based tools" | Sec. 4.3, two-step attacks | Authors' own |  |
| 17 | MANAGE 2.4: Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use. | "a human operator can take control of the AI system" | Sec. 3.1, R1 table (M1.1) | Authors' own |  |
| 18 | DE.CM-01: Networks and network services are monitored to find potentially adverse events | "raw network traffic is collected and normalized" | Sec. 4.2; Sec. 5.1 | Authors' own |  |
| 19 | DE.AE-02: Potentially adverse events are analyzed to better understand associated activities | "AI also conducts forensic analysis to assess damage and strengthen future defenses" | Sec. 4.2 | Reports other work or describes a risk/incident |  |
| 20 | MEASURE 2.4: The functionality and behavior of the AI system and its components - as identified in the map function - are monitored when in production. | "Continuous verification and early detection of anomalies or new hazards" | Sec. 3.9, R9 table (M9.7) | Authors' own |  |
| 21 | PR.PS-04: Log records are generated and made available for continuous monitoring | "All decisions are recorded in the audit ledger" | Sec. 4.3; Sec. 4.6 | Authors' own |  |
| 22 | GOVERN 1.4: The risk management process and its outcomes are established through transparent policies, procedures, and other controls based on organizational risk priorities. | "Policies are defined using a YAML schema that specifies conditions, actions, and supporting metadata." | Sec. 4.4 | Authors' own |  |
| 23 | DE.CM-01: Networks and network services are monitored to find potentially adverse events | "AI systems can continuously monitor network environments, detect anomalies" | Abstract p.106 | Authors' own |  |
| 24 | PR.DS-01: The confidentiality, integrity, and availability of data-at-rest are protected | "storage of data without adequate security measures such as encryption, access controls" | Sec. 4.1, Table 3 | Reports other work or describes a risk/incident |  |

## Part 2: Whose AI is it? (role of AI, per control)

For each control, write **D** (the organisation uses AI as part of its defence), **O** (the control protects or governs the organisation's own AI system) or **A** (the control responds to attackers using AI).

| # | Control described in the source | Your code (D/O/A) |
|---|---|---|
| 1 | Monitoring drift in the detector's input traffic |  |
| 2 | A tunable governance layer trades policy strictness against detection accuracy |  |
| 3 | Adversarial training of models |  |
| 4 | Incident response procedures for AI privacy breaches |  |
| 5 | Engineers and operators can override the AI intrusion detector |  |
| 6 | Access control and oversight mechanisms for AI systems |  |
| 7 | Comprehensive AI governance systems with risk procedures |  |
| 8 | AI automates incident response processes |  |
| 9 | AI predicts potential vulnerabilities before they are exploited |  |
| 10 | AI systems continuously monitor network environments and detect anomalies |  |
| 11 | Adversarial training of defensive models |  |
| 12 | Developing employees' digital skills |  |
| 13 | Threat hunting with AI and ML |  |
| 14 | Model predictions are checked against policy rules before they are executed |  |
| 15 | Safeguarding model inputs and enforcing model usage boundaries |  |
| 16 | Deceptive defence structures that create controlled compromised systems |  |
| 17 | Human-in-the-loop review |  |
| 18 | Explainable AI to see whether models were manipulated |  |
| 19 | Autonomous defence systems that use AI to analyse telemetry |  |
| 20 | Monitoring for AI-specific privacy patterns |  |
| 21 | All system decisions are recorded in an audit ledger |  |
| 22 | An AI-based system for detecting cyberattacks |  |
| 23 | ML-based anomaly and zero-day detection |  |

Date and time you finished: ____________

Signed: Gaurav Sharma