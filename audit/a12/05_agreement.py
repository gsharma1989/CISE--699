"""Agreement between Sanjeev Tiwari's independent coding and Claude's first pass on the fresh sample.
Q1: codability (Y/N) per source. Q3: main role = role of the first-listed control, compared where both coded Y."""
import csv, sys
from collections import Counter
def kappa(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[k] / n * cb[k] / n for k in set(ca) | set(cb))
    return po, (po - pe) / (1 - pe) if pe < 1 else float('nan')
S = {r['tracker_row']: r for r in csv.DictReader(open(sys.argv[1]))}
C = {r['tracker_row']: r for r in csv.DictReader(open(sys.argv[2]))}
ids = list(S)
q1s = [S[i]['q1_specific_control'][0] for i in ids]; q1c = [C[i]['q1_specific_control'][0] for i in ids]
po, k = kappa(q1s, q1c)
print(f"Q1 codability: {sum(x==y for x,y in zip(q1s,q1c))} of {len(ids)} agree, kappa {k:.2f}")
for i, a, b in zip(ids, q1s, q1c):
    if a != b: print("  Q1 disagreement", i, "Sanjeev", a, "Claude", b)
both = [i for i in ids if S[i]['q1_specific_control'][0] == 'Y' and C[i]['q1_specific_control'][0] == 'Y']
rs = [S[i]['q3_roles'].strip()[0] for i in both]; rc = [C[i]['q3_roles'].strip()[0] for i in both]
po, k = kappa(rs, rc)
print(f"Q3 main role (sources both coded Y, n={len(both)}): {sum(x==y for x,y in zip(rs,rc))} of {len(both)} agree, kappa {k:.2f}")
for i, a, b in zip(both, rs, rc):
    if a != b: print("  Role disagreement", i, "Sanjeev", S[i]['q3_roles'], "| Claude", C[i]['q3_roles'])
