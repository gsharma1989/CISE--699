# Risk and Issue Log

| ID | Description | Severity | Mitigation Action | Owner | Status |
|----|--------------|----------|--------------------|-------|--------|
| R-01 | Loss of access to a licensed database mid-review. | Medium | Fallback to Google Scholar or author-archived copies. | Gaurav Sharma | Occurred in a related form on 2026-10-29: Google Scholar blocked automated paging. Fallback used: same search string run in OpenAlex; query and rank recorded for every row. |
| R-02 | Single-reviewer screening bias, no second coder. | High | Spot-check a 10% random resample against original decisions; target at least 90% agreement at full scale. | Gaurav Sharma, pending supervisor sign-off | Open. 8 close-call re-checks done (all agreed), but the random 10% resample is still to do. |
| R-03 | Governance references still in draft or moving (Cyber AI Profile, COSAiS, EU AI Act phase-in). | Medium | Currency-flagging rule applied consistently: every moving-target source is dated and marked draft or in-force. | Gaurav Sharma | Mitigated |
| R-04 | English-language and database-coverage bias. | Low | Disclosed explicitly as a known limitation rather than hidden. | Gaurav Sharma | Accepted, disclosed |
| R-05 | Framework-to-governance mappings may not be one-to-one. | Medium | Many-to-many and unresolved mappings get recorded as-is rather than forced into a false single line. | Gaurav Sharma | Mitigated by design. Confirmed in Assignment 09: the NIST crosswalk maps some AI RMF subcategories to up to seven ISO controls. |
| R-06 | Pilot search or pilot screening turns up a problem with the protocol before full-scale screening starts. | Medium | That is the exact purpose of piloting at small scale first. | Gaurav Sharma | Mitigated; pilot found no issues |
| R-07 | Framework and regional bias: the three validation frameworks are US and EU standards, so findings may not transfer to other regions. | Low | Report as a limit; note sources that adapt the frameworks elsewhere (e.g., Chege & Wainaina, 2026, Kenya). | Gaurav Sharma | Open, disclosed |
| R-08 | Low-quality or non-peer-reviewed sources inflating the corpus. | Medium | Keep every screened source logged; flag low-weight sources; appraise all included sources before synthesis. | Gaurav Sharma | Open; appraisal scheduled |
