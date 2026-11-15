"""Compare the files a run produced with the expected SHA-256 values.

Usage:
  python analysis/verify_outputs.py <out_dir> audit/a11/expected_outputs.txt

Prints one line per file (MATCH or MISMATCH) and a final verdict. Works on Windows, macOS and Linux.
"""
import hashlib
import os
import sys


def main(out_dir, expected):
    ok = True
    for line in open(expected, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        want, name = line.split(None, 1)
        path = os.path.join(out_dir, name.strip())
        if not os.path.exists(path):
            print(f"MISSING   {name}")
            ok = False
            continue
        got = hashlib.sha256(open(path, "rb").read()).hexdigest()
        print(f"{'MATCH   ' if got == want else 'MISMATCH'}  {name}")
        ok = ok and got == want
    print("ALL OUTPUTS MATCH" if ok else "SOME OUTPUTS DIFFER - please report the lines above")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
