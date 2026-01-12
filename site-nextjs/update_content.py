#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    script = ROOT / "scripts" / "generate_site_content.py"
    subprocess.run([sys.executable, str(script), "--site", "nextjs"], check=True)


if __name__ == "__main__":
    main()
