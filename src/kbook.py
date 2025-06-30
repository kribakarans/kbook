#!/usr/bin/env python3

import os
import sys

# Use the installed shared path
INSTALL_DIR = os.path.expanduser("~/.local/kbook")
sys.path.insert(0, INSTALL_DIR)

from build_summary import build_summary
import generate_book

SUMMARY_PATH = os.path.join("chapters", "SUMMARY.md")

def main():
    if os.path.exists(SUMMARY_PATH):
        print(f"[i] Using existing {SUMMARY_PATH}")
    else:
        print("[*] Generating SUMMARY.md...")
        build_summary()

    print("[*] Generating HTML book...")
    generate_book.main()
    print("[✓] Done.")

if __name__ == "__main__":
    main()

