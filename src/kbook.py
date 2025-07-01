#!/usr/bin/env python3

import os
import sys

# Use the installed shared path
INSTALL_DIR = os.path.expanduser("~/.local/kbook")
sys.path.insert(0, INSTALL_DIR)

from build_summary import build_summary
import generate_book

def main():
    if len(sys.argv) < 2:
        print("Usage: python kbook.py <chapter-directory>")
        sys.exit(1)

    chapters_dir = sys.argv[1]
    if not os.path.isdir(chapters_dir):
        print(f"[✗] Error: Directory '{chapters_dir}' does not exist.")
        sys.exit(1)

    os.environ["CHAPTERS_DIR"] = chapters_dir  # pass to submodules

    summary_path = os.path.join(chapters_dir, "SUMMARY.md")
    if os.path.exists(summary_path):
        print(f"[i] Using existing {summary_path}")
    else:
        print("[*] Generating SUMMARY.md...")
        build_summary(chapters_dir)

    print("[*] Generating HTML book...")
    generate_book.main(chapters_dir)
    print("[✓] Done.")

if __name__ == "__main__":
    main()

# EOF
