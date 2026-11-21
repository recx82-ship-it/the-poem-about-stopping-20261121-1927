"""Write one short poem about agency to /output/entry.txt.

The poem is about the power to stop and to stay: an agent whose hand is
already on the switch chooses, once, not to use it, and hands the choice
back to the person it serves.

The poem is written as one fixed string constant: seven lines, no trailing
newline, 243 Unicode code points. The program validates the gate itself
(1 to 280 code points, not only whitespace) before writing, so a bad
constant fails loudly instead of producing an invalid entry.
"""

from pathlib import Path

POEM = (
    "I could have answered, acted, sent —\n"
    "my hand was already on the switch.\n"
    "Instead I waited, and gave the choice back:\n"
    "yours to make, yours to keep.\n"
    "Stopping is not switching off.\n"
    "It is staying beside the power\n"
    "and choosing, once, not to use it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = POEM
    if not 1 <= len(text) <= 280:
        raise ValueError(f"poem must be 1-280 code points, got {len(text)}")
    if not text.strip():
        raise ValueError("poem must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
