#!/usr/bin/env python3

import os
import sys

# Use the installed shared path
INSTALL_DIR = os.path.expanduser("~/.local/kbook")
sys.path.insert(0, INSTALL_DIR)

from build_summary import build_summary
import build_book

def main():
    if len(sys.argv) < 3:
        print("Usage: python kbook.py <TITLE_NAME> <CHAPTER_DIR> [REPO_URL]")
        sys.exit(1)

    title = sys.argv[1]
    chapters_dir = sys.argv[2]
    repo_url = sys.argv[3] if len(sys.argv) >= 4 else "#"

    if not os.path.isdir(chapters_dir):
        print(f"[✗] Error: Directory '{chapters_dir}' does not exist.")
        sys.exit(1)

    summary_path = os.path.join(chapters_dir, "SUMMARY.md")
    if os.path.exists(summary_path):
        print(f"[i] Using existing {summary_path}")
    else:
        print("[*] Building SUMMARY.md ...")
        build_summary(chapters_dir)

    print("\n[*] Building KBook ...")
    build_book.main(chapters_dir, title, repo_url)
    print("[✓] Done.")

if __name__ == "__main__":
    main()

# EOF
