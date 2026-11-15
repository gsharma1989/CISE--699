# Reproduction log for release a11-evidence-v1

## Run 1: fresh run by Claude (AI), not a human reproduction
- Date: 2026-11-15 (UTC)
- Who ran it: Claude (Anthropic), the AI research assistant that also wrote the scripts. This is a self-audit, not an independent check.
- Where: a new, empty Linux folder (Python 3.13.16, openpyxl 3.1.5 in a fresh virtual environment).
- What: downloaded the files of commit 82059ee (tagged a11-evidence-v1) and followed README Section 6 exactly, Steps 1-5.
- Result: verify_outputs.py printed MATCH for counts.txt, integrity_report.txt, iso_comparison.csv, sensitivity.txt and tracker_rows.csv, then ALL OUTPUTS MATCH. counts.txt: logged=60, included=45, excluded=15, included_not_peer_reviewed=12; integrity_report.txt: 0 warnings.
- An attempt to repeat the run on my Windows laptop was stopped before anything was installed: Python is not installed there, and the AI cannot type commands on that computer.

## Run 2: independent human reproduction - PENDING
Requested in the Hard Stop 5 feedback. To be done by me (Gaurav Sharma) or a classmate on a Windows laptop, following the README "Windows, step by step" instructions, and recorded here with the date, the person, the Python version, and the verify_outputs.py result.
