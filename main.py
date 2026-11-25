"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence (at most 200 characters) about the best meal
ever had to /output/entry.txt. Python standard library only.
"""

import os

ENTRY = (
    "At two in the morning, on a wobbling plastic stool, I ate nasi goreng "
    "still hissing from the wok, egg folded through the rice, and the street "
    "smelled of kecap and rain."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """Check the entry meets the competition gate: UTF-8, 1-200 chars,
    not only whitespace, a single sentence."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200 limit" % len(text))
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")
    text.encode("utf-8")
    return True


def write_entry(path, text):
    """Write the entry text to path, creating parent dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def verify_written_bytes(path, text):
    """Read back the file and confirm its bytes are exactly the entry."""
    with open(path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise RuntimeError("read-back mismatch: %s differs from ENTRY" % path)
    return written


def main():
    validate(ENTRY)
    write_entry(OUTPUT_PATH, ENTRY)
    verify_written_bytes(OUTPUT_PATH, ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), OUTPUT_PATH))


if __name__ == "__main__":
    main()
