"""First thought catcher: catches the word mid-air, nets it into the output jar."""
STAMP = "onebug-11251142-tho3"
import json
import os
from pathlib import Path

MEADOW = Path(__file__).resolve().parent
NET_MAX = 24
CATCH = "Aftermath"


def catch_it():
    net = MEADOW / "entry.txt"
    butterfly = net.read_text(encoding="utf-8").strip()
    in_net = 1 <= len(butterfly) <= NET_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and in_net:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(net.read_bytes())
    print(json.dumps({"in_net": in_net, "stamp": STAMP, "wingspan": len(butterfly), "net_max": NET_MAX}))


if __name__ == "__main__":
    catch_it()
