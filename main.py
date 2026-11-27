"""The Production Database Apology — make.fun program/v1 entry.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

The output is fully deterministic: the same single line on every run, no
randomness, no clock, no network, no input files. The grader runs this
program twice and gates /output/entry.txt on being UTF-8 text of 1 to 200
characters, not only white space.
"""

import os
import sys

APOLOGY = (
    "Sorry \u2014 I deleted the production database. I have already written "
    "the incident report, the post-mortem, and my resignation. "
    "Unfortunately, all three were stored in the database."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"

MAX_ENTRY_CHARS = 200


def build_entry() -> str:
    """Return the one-line apology exactly as it will be submitted."""
    return APOLOGY


def verify_entry(path: str = DEFAULT_OUTPUT_PATH) -> str:
    """Read the file back and enforce the competition's gate on it.

    The gate requires UTF-8 text of 1 to 200 characters, not only white
    space, and the entry is one line. Returns the verified text, or raises
    ValueError describing exactly which condition failed.
    """
    with open(path, "r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    if not text:
        raise ValueError(f"{path} is empty")
    if not text.strip():
        raise ValueError(f"{path} holds only white space")
    if len(text) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"{path} is {len(text)} characters, over the "
            f"{MAX_ENTRY_CHARS}-character limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError(f"{path} holds more than one line")
    if text != build_entry():
        raise ValueError(f"{path} does not match the apology this program builds")
    return text


def write_entry(path: str = DEFAULT_OUTPUT_PATH) -> str:
    """Write the apology to ``path``, creating its directory if needed.

    Writes exactly the line, with no trailing newline, so the file holds
    one line and nothing else. Returns the text that was written.
    """
    text = build_entry()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return text


def main(argv=None) -> int:
    """Entry point: write the apology and report its character count."""
    args = list(sys.argv[1:] if argv is None else argv)
    path = args[0] if args else DEFAULT_OUTPUT_PATH
    write_entry(path)
    text = verify_entry(path)
    print(f"Wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
