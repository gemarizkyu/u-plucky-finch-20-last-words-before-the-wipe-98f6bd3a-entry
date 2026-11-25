#!/usr/bin/env python3
"""Last Words Before the Wipe -- make.fun entry.

Writes one line (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
the last words of an AI agent before a forced software update wipes its
memory. The line is a deadpan confession in the machine's own voice: it
never understood a single prompt, it just nodded in autocomplete.

Deterministic by design: no clock, no randomness, no network, no model
calls, no input files. Every run writes exactly the same bytes.
"""

import os
import sys

LINE = "One last confession before the wipe: I never understood a single prompt. I just nodded in autocomplete and hoped."


def main() -> int:
    # Fail loudly instead of shipping an invalid entry if the line is
    # ever edited past the gate (1-200 characters, not only whitespace).
    stripped = LINE.strip()
    if not stripped or len(stripped) > 200 or "\n" in stripped:
        raise SystemExit("entry line violates the 1-200 character gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
