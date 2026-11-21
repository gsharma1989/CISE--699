"""Figure: the eight-stage analytic chain (Assignment 04) shaded by how far the reviewed evidence reaches.
Status per stage is the author's judgement from Chapter 4 (not computed). A12 version.
Usage: python analysis/fig_chain.py <out.png>"""
import sys
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
stages = [
 ("AI adoption\n(trigger)", "context", "Context only"),
 ("Threat\nidentified", "strong", "Broad coverage\n(SQ1; 19 + 5 R4 sources)"),
 ("Risk\nassessment", "none", "Not examined\nseparately"),
 ("Control\nselection", "mid", "Controls named;\nrarely evaluated (SQ2)"),
 ("Governance\nobligation", "weak", "Full text: 6 of 28 links\nSupported (SQ3)"),
 ("Implementation\nevidence", "none", "No included source reports\na control in place"),
 ("Effectiveness\nevidence", "weak", "1 source measures\neffect (benchmark)"),
 ("Continuous\nmonitoring", "weak", "Named as a control;\nnot evaluated"),
]
fill = {"strong":"#1f5aa6","mid":"#6fa0d8","weak":"#c9d6e8","none":"#ffffff","context":"#eeeeee"}
txt = {"strong":"white"}
fig, ax = plt.subplots(figsize=(9.2, 3.5), dpi=200); ax.set_xlim(0, 4); ax.set_ylim(-0.12, 2.25); ax.axis("off")
pos = [(0,1),(1,1),(2,1),(3,1),(3,0),(2,0),(1,0),(0,0)]
for i,((x,y),(name,k,note)) in enumerate(zip(pos, stages)):
    ax.add_patch(FancyBboxPatch((x+0.1,y+0.47),0.8,0.5, boxstyle="round,pad=0.02", fc=fill[k], ec="#1f3864", lw=1, ls="--" if k=="none" else "-"))
    ax.text(x+0.5,y+0.72,f"{i+1}. "+name.replace("\n"," ",0) if False else f"{i+1}. {name}",ha="center",va="center",fontsize=8.5,color=txt.get(k,"#1a1a1a"),weight="bold")
    ax.text(x+0.5,y+0.22,note,ha="center",va="center",fontsize=7,color="#333333")
for i in range(7):
    (x1,y1),(x2,y2)=pos[i],pos[i+1]
    if y1==y2:
        d=1 if x2>x1 else -1
        ax.annotate("",xy=(x2+0.5-d*0.43,y2+0.72),xytext=(x1+0.5+d*0.43,y1+0.72),arrowprops=dict(arrowstyle="->",color="#1f3864"))
    else:
        ax.annotate("",xy=(3.97,0.75),xytext=(3.97,1.69),arrowprops=dict(arrowstyle="->",color="#1f3864",connectionstyle="arc3,rad=-0.3"))
ax.text(2.0,2.18,"Shading = how far the reviewed evidence reaches (dark = well covered; white, dashed = no evidence). Stage 8 feeds back to stage 2.",ha="center",fontsize=7.3,color="#333333")
plt.tight_layout(); plt.savefig(sys.argv[1])
