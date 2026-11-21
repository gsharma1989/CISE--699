"""Cross-check (A12): every key number in the thesis and the deck against the record outputs.
Usage: python audit/a12/14_crosscheck.py <out_dir> <thesis.txt> <deck.txt>
Each check recomputes the value from a record file and searches for the stated phrase in the documents."""
import csv, re, sys, collections
out, thesis, deck = sys.argv[1:4]
T = re.sub(r"\s+", " ", open(thesis, encoding="utf-8").read())
D = re.sub(r"\s+", " ", open(deck, encoding="utf-8").read())
c = dict(l.strip().split("=", 1) for l in open(f"{out}/counts.txt", encoding="utf-8") if "=" in l and not l.startswith(" "))
fc = list(csv.DictReader(open("audit/a12/03_fulltext_coding_claude.csv", encoding="utf-8")))
ft = collections.Counter(r["claude_verdict_v12"].split(" (")[0] for r in fc if r["location"] != "abstract")
ag = open("audit/a12/05_agreement_result.txt", encoding="utf-8").read()
rr = open(f"{out}/role_retest.txt", encoding="utf-8").read()
tr = {r["tracker_row"]: r["tier"] for r in csv.DictReader(open("audit/hs5/08_quality_appraisal.csv", encoding="utf-8"))}
tr.update({r["tracker_id"]: (r.get("tier_author") or r["tier_proposed"]) for r in csv.DictReader(open("audit/a12/08_atlas_screening.csv", encoding="utf-8")) if r.get("tier_author") or r["tier_proposed"]})
inc = [r["id"] for r in csv.DictReader(open(f"{out}/tracker_rows.csv", encoding="utf-8")) if r["decision"] == "Include"]
tc = collections.Counter(tr[i] for i in inc)
pr = collections.Counter(r["status"].split(" (")[0] for r in csv.DictReader(open("audit/a12/06_prisma2020_checklist.csv", encoding="utf-8")))
checks = [
 ("logged 80", c["logged"] == "80", ["80 logged, 56 included, 24 excluded", "Done: 80 screened"]),
 ("included 56", c["included"] == "56", ["56 were included", "56 used"]),
 ("not peer reviewed 17", c["included_not_peer_reviewed"].startswith("17"), ["Seventeen are not peer reviewed", "17 of 56 sources are not peer reviewed"]),
 ("full text 28 links", sum(ft.values()) == 28, ["28 links", "28 links"]),
 ("6 S / 14 P / 7 NS / 1 gap", (ft["Supported"], ft["Partly"], ft["Not supported"], ft["Evidenced gap"]) == (6, 14, 7, 1), ["6 S, 14 P, 7 NS, 1 gap", "6 Supported, 14 Partly, 7 Not supported, 1 gap"]),
 ("Q1 7/8 kappa 0.60", "7 of 8 agree, kappa 0.60" in ag, ["7 of 8, kappa 0.60", "7 of 8 (kappa 0.60)"]),
 ("role 4/6 kappa 0.43", "4 of 6 agree, kappa 0.43" in ag, ["4 of 6, kappa 0.43", "kappa 0.43"]),
 ("5 of 41 roles changed", "5 of 41" in rr, ["5 of 41 coded links change role", None]),
 ("PRISMA 30/8/2/2", (pr["Met"], pr["Partly met"], pr["Not met"], pr["Not applicable"]) == (30, 8, 2, 2), ["30 met, 8 partly, 2 not met", "30 met, 8 partly, 2 not met"]),
 ("tiers 11/24/21", (tc["1"], tc["2"], tc["3"]) == (11, 24, 21), ["11 sources are Tier 1, 24 Tier 2 and 21 Tier 3", "solid method | 11"]),
]
ok = True
for name, rec, (tp, dp) in checks:
    t_ok = tp is None or tp in T
    d_ok = dp is None or dp in D
    ok &= rec and t_ok and d_ok
    print(f"{'OK  ' if rec and t_ok and d_ok else 'FAIL'} {name}: record={rec} thesis={t_ok} deck={d_ok if dp else 'n/a'}")
print("CROSS-CHECK PASSED" if ok else "CROSS-CHECK FAILED")
