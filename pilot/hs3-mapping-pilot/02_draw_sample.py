"""Draw the HS3 pilot sample.

Usage: python3 02_draw_sample.py ../screening/Screening_Tracker_Full_Scale.xlsx
Frame: included tracker rows not clause-mapped in Assignment 09.
"""
import random
import sys

import openpyxl

MAPPED_IN_A09 = {1, 2, 3, 4, 5, 6, 8, 17, 18, 52, 14, 21, 50}  # 10 mapped + 3 contrast rows
SEED = 20261107
N = 8

wb = openpyxl.load_workbook(sys.argv[1])
ws = wb["Screening Tracker"]
frame = []
for r in range(2, ws.max_row + 1):
    title = ws.cell(r, 2).value
    if not title:
        continue
    row_no = r - 1
    if ws.cell(r, 8).value == "Include" and row_no not in MAPPED_IN_A09:
        frame.append(row_no)

sample = sorted(random.Random(SEED).sample(frame, N))
print(f"frame_size={len(frame)} seed={SEED} n={N}")
print("frame=" + ",".join(map(str, frame)))
print("sample=" + ",".join(map(str, sample)))
