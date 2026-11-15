# Reproduction log for release a11-evidence-v1

## Run 1: fresh run by Claude (AI), not a human reproduction
- Date: 2026-11-15 (UTC)
- Who ran it: Claude (Anthropic), the AI research assistant that also wrote the scripts. This is a self-audit, not an independent check.
- Where: a new, empty Linux folder (Python 3.13.16, openpyxl 3.1.5 in a fresh virtual environment).
- What: downloaded the files of commit 82059ee (tagged a11-evidence-v1) and followed README Section 6 exactly, Steps 1-5.
- Result: verify_outputs.py printed MATCH for counts.txt, integrity_report.txt, iso_comparison.csv, sensitivity.txt and tracker_rows.csv, then ALL OUTPUTS MATCH. counts.txt: logged=60, included=45, excluded=15, included_not_peer_reviewed=12; integrity_report.txt: 0 warnings.
- An attempt to repeat the run on my Windows laptop was stopped before anything was installed: Python is not installed there, and the AI cannot type commands on that computer.

## Run 2: human reproduction by Gaurav Sharma (Windows laptop) - DONE
- Date: 2026-11-15, 12:23 local time (timestamp printed by the run: "Sun 11/15/2026 12:23:07.81").
- Who ran it: Gaurav Sharma (student author), on his own Windows laptop. A human run on a different computer, operating system and Python version from Run 1. It is not independent of the author; a run by a classmate would be stronger and is still welcome.
- Software: Python 3.15.2 (python.org Python Install Manager, newer than the tested 3.13), openpyxl 3.1.5 installed with pip. No virtual environment was used.
- Files: the release folder CISE--699-a11-evidence-v1 (tag a11-evidence-v1, commit 82059ee), downloaded and extracted on the laptop. Claude checked three input files against the tag by SHA-256 and all match: Screening_Tracker_Full_Scale.xlsx 503f886c..., audit/a11/expected_outputs.txt 22067f13..., README.md d942c39a...
- How it was run: typing the commands was difficult, so Claude wrote a helper file (04b_run2_helper_RUN_ME_reproduction.bat). It contains only the README Windows commands (pip install openpyxl==3.1.5, then rebuild_counts, check_tracker, compare_a09_iso, sensitivity and verify_outputs, unchanged) and saves the screen output to a text file. Claude placed only this helper file in the release folder; no other file was added or changed. Gaurav started the run by double-clicking the helper in the release folder. Claude did not run any command on the laptop.
- Result: verify_outputs.py printed MATCH for counts.txt, integrity_report.txt, iso_comparison.csv, sensitivity.txt and tracker_rows.csv, then ALL OUTPUTS MATCH. counts.txt: logged=60, included=45, excluded=15, undecided=0, included_not_peer_reviewed=12. Full output: 04a_run2_output_windows.txt.
- Notes: pip printed a harmless notice that a newer pip exists. The README Windows steps worked with Python 3.15.2 on Windows, which was marked "not tested" before.
