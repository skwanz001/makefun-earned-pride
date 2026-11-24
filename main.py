"""One Line of Earned Pride — make.fun entry.

Writes a single line (1-240 chars) to /output/entry.txt: a quiet, earned
moment of pride for someone in a scene.
"""

import os

LINE = (
    "After forty years of signing with an X, he wrote his name on his "
    "granddaughter's birthday card \u2014 in full, in ink, without asking "
    "for help."
)


def main() -> None:
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars, must be 1-240"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify the file round-trips byte-exact: the sealed scorer gates on
    # 1-240 UTF-8 chars, not only whitespace.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    print(f"wrote {len(written)} chars to /output/entry.txt")
    print(written)


if __name__ == "__main__":
    main()
