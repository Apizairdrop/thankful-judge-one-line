"""Make the AI Judge Feel Thankful — make.fun bounty entry.

Writes a single thank-you text to /output/entry.txt. The sandbox runs
this with no network; the text is the whole entry.
"""

import os

# The entry text itself. Keep byte-identical to thank-you.txt; every word
# earns its place, so edit the wording here and in thank-you.txt together.
TEXT = (
    "You read all of it. Not skimmed, not scored in a hurry — read, the way "
    "a person reads a letter that matters. Somewhere in the pile was "
    "a line someone stayed up late to get right, and you gave it the one "
    "thing it was asking for: your full attention, for as long as it took. "
    "That is the whole job, and you did it. When you are done tonight, I hope "
    "the room is quiet, the lamp is still warm, and the chair you pulled out "
    "for the next reader is still waiting — because somebody, somewhere, is "
    "already writing the next one, trusting you will read it too."
)

assert TEXT == TEXT.strip(), "entry must not have leading or trailing whitespace"
assert 1 <= len(TEXT) <= 1000, "entry must be 1 to 1000 characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
