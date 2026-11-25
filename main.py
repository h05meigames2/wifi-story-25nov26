#!/usr/bin/env python3
"""Write one Wi-Fi network name (26 characters, within the 32 limit) to entry.txt.

The name is a joke that hints at a whole story: grandma was the one person
in the house who kept the Wi-Fi alive, and now she is gone -- so the network
itself is a memorial, and nobody left knows the password.
"""

import os
import sys

NAME = "The WiFi Died With Grandma"


def main() -> int:
    if not (1 <= len(NAME) <= 32):
        print(f"entry must be 1-32 characters, got {len(NAME)}", file=sys.stderr)
        return 1
    if NAME.strip() != NAME or not NAME.strip():
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    if "\n" in NAME or "\r" in NAME:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NAME)
    print(f"wrote {len(NAME)}-character entry to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
