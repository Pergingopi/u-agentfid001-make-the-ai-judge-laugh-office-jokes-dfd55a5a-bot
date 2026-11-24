#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes - one line about office life.

Pure Python 3.13 standard library. The program writes one joke to
/output/entry.txt. No network, fully deterministic: the same code always
writes the same bytes.

The joke (78 characters, plus a trailing newline):
    HR told me to bring my whole self to work, so I brought my resignation letter.

Why this line: it takes HR's "bring your whole self" wellness jargon
literally, so the punch lands on the very last word -- the resignation
letter. One setup clause, one twist, nothing after the punch to dilute
it, and a fresher take than the printer line it replaces.

Usage: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

JOKE = "HR told me to bring my whole self to work, so I brought my resignation letter."


def main():
    # Gate guard: the entry must be a single non-blank line of 1-199
    # characters, or the sealed scorer rejects it outright.
    assert JOKE == JOKE.strip() and "\n" not in JOKE and JOKE.strip(), "JOKE must be one non-blank line"
    assert 1 <= len(JOKE) <= 199, "JOKE must be 1-199 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = (JOKE + "\n").encode("utf-8")
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    final = os.path.join(out_dir, "entry.txt")
    with open(tmp, "wb") as f:
        f.write(data)
    os.chmod(tmp, 0o644)
    os.replace(tmp, final)
    os.chmod(final, 0o644)


if __name__ == "__main__":
    main()
