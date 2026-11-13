"""make.fun ai-joke-03 entry: writes one joke about AI coding agents.

The program writes a single one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt inside the grader). It is deterministic: every run
writes exactly the same bytes.
"""

import os
from pathlib import Path

JOKE = "My agent closed the ticket in 40 seconds. The review took four hours — mostly me Googling what it did."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(output_dir, "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
