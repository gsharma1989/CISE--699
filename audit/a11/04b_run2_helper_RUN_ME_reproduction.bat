@echo off
cd /d "%~dp0"
set PY=python
where py >nul 2>nul && set PY=py
echo Running the README checks. Please wait...
(
echo Run date: %date% %time%
echo Folder: %cd%
%PY% --version
%PY% -m pip install openpyxl==3.1.5
%PY% analysis/rebuild_counts.py screening/Screening_Tracker_Full_Scale.xlsx out
%PY% analysis/check_tracker.py screening/Screening_Tracker_Full_Scale.xlsx out
%PY% analysis/compare_a09_iso.py mapping/a09_proof_map_links.csv pilot/hs3-mapping-pilot/04_crosswalk_ai-rmf_to_iso42001.csv pilot/hs3-mapping-pilot/05_annexA_controls.csv out
%PY% analysis/sensitivity.py out/tracker_rows.csv mapping/a09_proof_map_links.csv out
%PY% analysis/verify_outputs.py out audit/a11/expected_outputs.txt
) > reproduction_output.txt 2>&1
type reproduction_output.txt
echo.
echo Finished. The full output is saved in reproduction_output.txt in this folder.
pause
