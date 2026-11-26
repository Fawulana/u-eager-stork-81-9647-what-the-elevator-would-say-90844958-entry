"""What the Elevator Would Say -- make.fun entry.

Writes the funniest one line a talking elevator could say to
/output/entry.txt. Deterministic, offline, standard library only:
the same single line is written on every run.
"""

import os

LINE = "You pressed the button twice. I'm not faster now \u2014 I'm just disappointed in you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
