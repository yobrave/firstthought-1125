# firstthought reentry: drops the chosen single word into the gate folder
import json, os, pathlib

PICK = "petrichor"
SLOT_NAME = "entry.txt"
CEILING = 24


def shaped(blob: str) -> dict:
    tidy = blob.strip()
    lone = (len(tidy.split()) == 1) and tidy.isalpha()
    roomy = len(tidy) <= CEILING
    return {"pick": tidy, "lone": lone, "roomy": roomy, "green": lone and roomy}


def deliver() -> None:
    yard = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
    yard.mkdir(parents=True, exist_ok=True)
    slot = yard / SLOT_NAME
    with open(slot, "w", encoding="utf-8", newline="\n") as pen:
        pen.write(PICK + "\n")
    with open(slot, "r", encoding="utf-8") as pen:
        mirror = pen.read().strip()
    facts = shaped(mirror)
    facts["mirror"] = mirror == PICK
    facts["note"] = "reentry-1125"
    print(json.dumps(facts, sort_keys=True))


deliver()
