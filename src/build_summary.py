import os
import sys

def build_summary(chapters_dir):
    summary_file = os.path.join(chapters_dir, "SUMMARY.md")

    chapter_dirs = sorted([
        d for d in os.listdir(chapters_dir)
        if os.path.isdir(os.path.join(chapters_dir, d))
    ])

    lines = []

    print(f"[•] Found {len(chapter_dirs)} chapter folders")
    for chapter in chapter_dirs:
        chapter_title = chapter.replace('-', ' ').replace('_', ' ').title()
        lines.append(f"# {chapter_title}")
        print(f"[+] Chapter: {chapter_title}")

        chapter_path = os.path.join(chapters_dir, chapter)
        files = sorted([
            f for f in os.listdir(chapter_path)
            if os.path.isfile(os.path.join(chapter_path, f))
        ])

        for file in files:
            name = os.path.splitext(file)[0].replace('-', ' ').replace('_', ' ').title()
            rel_path = f"{chapter}/{file}"
            line = f"- [{name}]({rel_path})"
            lines.append(line)
            print(f"    [•] Subchapter: {line}")

        lines.append("")

    print(f"[✓] Writing to {summary_file}...")
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[✓] Generated {summary_file} successfully.")

# Optional CLI support
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python build_summary.py <chapter-directory>")
        sys.exit(1)

    target_dir = sys.argv[1]
    if not os.path.isdir(target_dir):
        print(f"[✗] Error: Directory '{target_dir}' does not exist.")
        sys.exit(1)

    build_summary(target_dir)

# EOF
