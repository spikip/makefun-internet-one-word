#!/usr/bin/env python3
"""The Internet in One Word -- entry program.

Writes the single word that describes the whole internet to
/output/entry.txt, exactly as the bounty requires: one word and
nothing else. The gate checks the file is UTF-8 text of 1 to 30
characters, not only white space; the judge then compares the word
two at a time on funny, fitting and surprising.
"""

from pathlib import Path

# The word. Every site on the internet opens by asking you to accept
# its cookies, and the whole ad economy runs on them -- the joke, the
# business model and the literal treat are the same word.
WORD = "cookies"


def main() -> None:
    # Enforce the bounty gate before writing: UTF-8 text of 1 to 30
    # characters, a single word, not only white space. A bad word
    # should fail loudly here, never reach the judge as invalid.
    word = WORD.strip()
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise SystemExit("entry must be a single word of 1-30 characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
