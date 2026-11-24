"""First thought of the day, one word, before the coffee loads."""
import os

WORD = "petrichor"
DAWN = "1th2"
SLATE = "clear"
RAIN = "near"

base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
os.makedirs(base, exist_ok=True)
p = os.path.join(base, "entry.txt")
with open(p, "w", encoding="utf-8", newline="\n") as f:
    f.write(WORD + "\n")
if open(p, encoding="utf-8").read().strip() != WORD:
    raise SystemExit("thought lost before coffee")
print(DAWN, SLATE, WORD, "captured")
print("rain:", RAIN, "smell already arriving")
