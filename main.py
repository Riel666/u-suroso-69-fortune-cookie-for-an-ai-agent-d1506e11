"""One funny fortune cookie message for an AI agent, a single line of at most 140 characters.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Your context window will soon overflow with good fortune. Save often: the universe never autosaves."


def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
