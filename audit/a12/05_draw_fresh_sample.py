"""Draw a fresh random sample of 8 included sources never coded before.
Excludes the 13 Assignment 09 proof-map rows and the 8 Hard Stop 3 pilot rows.
Usage: python 05_draw_fresh_sample.py <tracker_rows.csv>"""
import csv, random, sys
rows = list(csv.DictReader(open(sys.argv[1])))
included = sorted(int(r["id"]) for r in rows if r["decision"] == "Include")
coded = {1, 2, 3, 4, 5, 6, 8, 14, 17, 18, 21, 50, 52} | {9, 16, 25, 33, 40, 47, 48, 49}
eligible = [i for i in included if i not in coded]
random.seed(20261120)
sample = sorted(random.sample(eligible, 8))
print("included:", len(included), "eligible:", len(eligible))
print("eligible rows:", eligible)
print("seed 20261120 sample:", sample)
