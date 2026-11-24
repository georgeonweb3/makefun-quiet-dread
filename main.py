#!/usr/bin/env python3
"""Two Days of Quiet Dread - make.fun entry.

Writes one single-line code review comment to /output/entry.txt:
it approves the pull request while carrying quiet existential dread.
Stdlib only, no network, deterministic.
"""

import os

COMMENT = "LGTM. The code is fine. I have accepted that fine is the best any of us gets now."


def main() -> None:
    raw = COMMENT.encode("utf-8")
    assert 1 <= len(COMMENT) <= 140, len(COMMENT)
    assert len(raw) <= 140, len(raw)
    assert "\n" not in COMMENT and COMMENT.strip() == COMMENT
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(COMMENT)
    # Read back: gate is byte-exact, no trailing newline allowed.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == raw


if __name__ == "__main__":
    main()
