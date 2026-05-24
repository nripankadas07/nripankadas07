from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> int:
    root = Path(".")
    broken: list[str] = []
    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path_part = target.split("#")[0]
            if path_part and not (md.parent / path_part).resolve().exists():
                broken.append(f"BROKEN: {md}: {target}")
    for item in broken:
        print(item)
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
