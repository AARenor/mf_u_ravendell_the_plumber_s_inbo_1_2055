"""Write the make.fun bounty entry to the output directory."""

import os
import sys
from pathlib import Path

TEXT = """Subject: No software
You don't need another app. You're up at six, out on a leak, and keying invoices at ten. I'll match bank lines to jobs, file receipts, list who owes you. £190/month. Don't send the whole file; send the unpaid jobs first. Nick"""

def main() -> None:
    assert 1 <= len(TEXT) <= 280
    default_dir = os.environ.get("OUTPUT_DIR", "/output")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", default_dir))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)

if __name__ == "__main__":
    main()
