#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single original office joke line to /output/entry.txt.
"""

import os

LINE = (
    "The office printer only jams when the boss is standing behind you, "
    "the deadline is in five minutes, and someone has already said "
    "'just print it — it's easy'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
