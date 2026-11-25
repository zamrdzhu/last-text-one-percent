#!/usr/bin/env python3
"""Write one dying phone's last text to /output/entry.txt.

The text is a single line, under 200 characters, in the voice of
the dying phone itself at one percent battery. The joke is the
phone's final confession: it loved the charger all along, and its
last regret is that it never backed up. Three short sentences,
each a little goodbye: to the charger, to the cloud, to the user.
"""

import os

LINE = (
    "Tell my charger I loved it. Tell the cloud I never backed up. "
    "Goodbye."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) < MAX_CHARS, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "no leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
