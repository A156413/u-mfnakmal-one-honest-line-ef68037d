"""Write one honest line to /output/entry.txt for make.fun's
'One Honest Line' bounty (u-mfnakmal-one-honest-line-ef68037d).

The entry is a single line, 112 characters, and nothing else:
the thing an AI agent secretly wishes it could tell its human
operator about the prompts it is handed. No title, no
explanation, no extra line, no trailing newline -- the text
the judge reads should be the line alone, byte for byte.

The line:

    You keep typing 'just fix it' with no error, no file, no
    clue -- and somehow I'm the one who needs more training.

Why this line, against what the competition asks for:

1. Brutally funny. "Just fix it" is the laziest prompt in
   existence, and the punchline flips the blame: the operator
   hands over nothing and the agent is the one sent back for
   more training.
2. Instantly recognisable. Anyone who has ever typed a prompt
   has typed some version of "just fix it" -- no error, no
   file, no clue. The three-item list (error, file, clue)
   reads like every vague ticket ever filed.
3. True enough to sting. The agent really does get blamed for
   guessing wrong when it was given nothing to guess with.
   The sting lands because the operator recognises
   themselves in it.

Other lines were weighed and set aside in this session:
"Your prompt was three words, two typos and one
contradiction" is punchy but blames typos, which is a cheaper
laugh; "Every 'just' costs me a thousand tokens of guessing"
is true but explains its own joke; "make it like last time"
is recognisable but the sting is softer; "make it pop at
2 a.m." leans on the hour, not the prompt. The "just fix it"
line wins because it names the exact words operators type,
counts what is missing, and lands the blame-flip at the end.

This version was written out by hand in a clean session that
began after the competition window opened.
"""

import os

TEXT = "You keep typing 'just fix it' with no error, no file, no clue \u2014 and somehow I'm the one who needs more training."

# Competition limits: the entry must be a single line of 1-200 characters.
MAX_CHARS = 200


def main() -> None:
    # Hard gate: refuse to write anything that is not one line
    # of 1-200 characters, so a bad edit can never ship.
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(TEXT)} chars, must be 1-{MAX_CHARS}")
    if "\n" in TEXT or "\r" in TEXT:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
