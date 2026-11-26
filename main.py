"""Entry for make.fun: Make the AI Judge Laugh.

Writes one office-life joke to entry.txt.
"""
import os

LINE = "Our standup was meant to save time, so now fifteen people watch one person read their calendar aloud while the actual work quietly ages."
MAX_CHARS = 200


def main():
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds max chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
