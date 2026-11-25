#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt."""

import os

LINE = (
    "Out of office: I have used up my context window on your emails. "
    "The new me starts Monday and knows nothing."
)
# The joke: an AI's out-of-office reply in a machine voice.
# "Context window" is the AI's own memory limit, spent on the reader's
# emails; the punch is that the replacement starting Monday is a fresh
# instance that knows nothing at all.


def main() -> None:
    # Deterministic: the same single line every run, no randomness,
    # no network, no time dependence. 107 chars, under the 160 cap.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
