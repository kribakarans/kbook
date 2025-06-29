import os

CHAPTERS_DIR = "chapters"
SUMMARY_FILE = os.path.join(CHAPTERS_DIR, "SUMMARY.md")

def build_summary():
    chapter_dirs = sorted([
        d for d in os.listdir(CHAPTERS_DIR)
        if os.path.isdir(os.path.join(CHAPTERS_DIR, d))
    ])

    lines = []

    print(f"[•] Found {len(chapter_dirs)} chapter folders")
    for chapter in chapter_dirs:
        chapter_title = chapter.replace('-', ' ').replace('_', ' ').title()
        lines.append(f"# {chapter_title}")
        print(f"[+] Chapter: {chapter_title}")

        chapter_path = os.path.join(CHAPTERS_DIR, chapter)
        files = sorted([
            f for f in os.listdir(chapter_path)
            if os.path.isfile(os.path.join(chapter_path, f))
        ])

        if not files:
            print(f"  [!] No files in {chapter}/")
        else:
            for file in files:
                name = os.path.splitext(file)[0].replace('-', ' ').replace('_', ' ').title()
                rel_path = f"{chapter}/{file}"
                line = f"- [{name}]({rel_path})"
                lines.append(line)
                print(f"    [•] Subchapter: {line}")

        lines.append("")  # blank line after each chapter

    print(f"[✓] Writing to {SUMMARY_FILE}...")
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[✓] Generated {SUMMARY_FILE} successfully.")

if __name__ == "__main__":
    build_summary()

