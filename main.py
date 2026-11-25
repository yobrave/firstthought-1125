import json
import os
from collections import deque

SPARK = "tho3-first"
REACH = 24


def scan(blob):
    q = deque(blob.replace("\r", "").split("\n"))
    while q:
        row = q.popleft()
        if row.strip():
            return row
    return ""


def crown(line, root):
    dais = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(dais, exist_ok=True)
    medal = os.path.join(dais, "entry.txt")
    ink = line.encode("utf-8")
    with open(medal, "wb") as quill:
        quill.write(ink)
    with open(medal, "rb") as herald:
        if herald.read() != ink:
            raise RuntimeError("crown tarnished")
    return medal


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as mind:
    line = scan(mind.read())

if not line.strip() or len(line) > REACH:
    print(json.dumps({"crown": "blank", "size": len(line)}))
    raise SystemExit(1)
medal = crown(line, root)
print(json.dumps({"crown": line, "size": len(line), "reach": REACH, "spark": SPARK, "medal": os.path.basename(medal)}))
