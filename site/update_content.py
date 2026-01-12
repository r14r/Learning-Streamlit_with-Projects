#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent


def main() -> None:
    script = SITE_DIR / "build_site.py"
    subprocess.run([sys.executable, str(script)], check=True)


if __name__ == "__main__":
    main()
