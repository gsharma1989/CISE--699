"""Figure: included sources by category and quality tier.
Inputs (release a12-evidence-v1): out/tracker_rows.csv (from analysis/rebuild_counts.py),
audit/hs5/08_quality_appraisal.csv (rows 1-60) and audit/a12/08_atlas_screening.csv (rows 61-80; the author's tier where given, else the proposed tier).
Usage: python analysis/fig_tiers.py <repo_root> <out.png>"""
import csv, sys, collections
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
root, outp = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(f"{root}/out/tracker_rows.csv")))
tier = {r["tracker_row"]: r["tier"] for r in csv.DictReader(open(f"{root}/audit/hs5/08_quality_appraisal.csv"))}
tier.update({r["tracker_id"]: (r.get("tier_author") or r["tier_proposed"]) for r in csv.DictReader(open(f"{root}/audit/a12/08_atlas_screening.csv", encoding="utf-8")) if r.get("tier_author") or r["tier_proposed"]})
inc = [r for r in rows if r["decision"] == "Include"]
cats = ["Security controls","Security risks","AI-related threats","Governance risks","Compliance risks","Privacy risks","Human/organizational risks"]
c = collections.Counter((r["category"], tier[r["id"]]) for r in inc)
fig, ax = plt.subplots(figsize=(8.6, 4.1), dpi=200)
cols = {"1":"#1f5aa6","2":"#6fa0d8","3":"#c9d6e8"}
lab = {"1":"Tier 1: peer reviewed, stated method suited to claim","2":"Tier 2: peer reviewed, descriptive or no evaluation","3":"Tier 3: not peer reviewed, unclear, or serious flags"}
y = list(range(len(cats)))[::-1]
left = [0]*len(cats)
for t in ["1","2","3"]:
    vals = [c[(k,t)] for k in cats]
    ax.barh(y, vals, left=left, color=cols[t], edgecolor="white", label=lab[t], height=0.62)
    for yi, v, l in zip(y, vals, left):
        if v: ax.text(l+v/2, yi, str(v), ha="center", va="center", fontsize=8.5, color="white" if t=="1" else "#1a1a1a")
    left = [a+b for a,b in zip(left, vals)]
for yi, tot in zip(y, left): ax.text(tot+0.15, yi, str(tot), va="center", fontsize=9)
ax.set_yticks(y); ax.set_yticklabels(cats, fontsize=9)
ax.set_xlim(0, 17); ax.set_xlabel(f"Included sources (n = {len(inc)})", fontsize=9)
ax.spines[["top","right"]].set_visible(False); ax.tick_params(axis="x", labelsize=8)
ax.legend(fontsize=7.5, loc="lower right", frameon=False)
plt.tight_layout(); plt.savefig(outp)
print({t: sum(c[(k,t)] for k in cats) for t in "123"})
