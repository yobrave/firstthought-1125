"""Builds the one-word entry for One Word, First Thought (make.fun program/v1)."""
import json
import os
from pathlib import Path

WORD = "thagomizer"
GATE_MIN = 1
GATE_MAX = 24


def stamp(word: str) -> dict:
    trimmed = word.strip()
    single = len(trimmed.split()) == 1
    within = GATE_MIN <= len(trimmed) <= GATE_MAX
    if not (single and within):
        raise SystemExit(f"gate rejected: {trimmed!r} single={single} within={within}")
    return {"word": trimmed, "chars": len(trimmed), "gate": "pass", "voice": "first-thought"}


def main() -> None:
    receipt = stamp(WORD)
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(WORD + "\n", encoding="utf-8")
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
