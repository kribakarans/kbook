import os
import re
import sys

HOME_DIR = os.path.expanduser("~")
PREFIX = os.path.join(HOME_DIR, ".local", "kbook", "html")
TEMPLATE_FILE = os.path.join(PREFIX, "index.html.in")
OUTPUT_FILE = "index.html"

# Regex pattern for [Title](path)
link_pattern = re.compile(r"\[\s*(.*?)\s*\]\(\s*(.*?)\s*\)")

def parse_summary_to_html(summary_file):
    with open(summary_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    html_lines = []
    subchapter_refs = []
    chapter_count = 0
    sub_count = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            chapter_count += 1
            sub_count = 0
            chapter_title = stripped[2:].strip()
            chapter_id = f"chapter_{chapter_count}"
            escaped_title = chapter_title.replace("'", "\\'").replace('"', '\\"')
            html_lines.append("")
            html_lines.append(
                f'        <h3><b><a href="#" onclick="showSubChapters(\'{chapter_id}\', \'{escaped_title}\', \'{chapter_count}\')">{chapter_count}. {chapter_title}</a></b></h3>'
            )
            subchapter_refs.append((chapter_id, []))
        elif match := link_pattern.search(stripped):
            sub_count += 1
            title, path = match.groups()
            index = f"{chapter_count}.{sub_count}"
            escaped_sub = title.replace("'", "\\'").replace('"', '\\"')
            html_lines.append(
                f'        <div style="margin-left:1em;"><a href="#" onclick="loadMarkdown(\'{path}\', \'{escaped_title}\', \'{escaped_sub}\')">{index}. {title}</a></div>'
            )
            subchapter_refs[-1][1].append((index, title, path))

    # JS map for subchapters
    js_map = "window.chapterMap = {\n"
    for cid, items in subchapter_refs:
        js_map += f'  "{cid}": [\n'
        for idx, title, path in items:
            js_map += f'    {{ index: "{idx}", title: "{title}", path: "{path}" }},\n'
        js_map += "  ],\n"
    js_map += "};\n"

    return "\n".join(html_lines) + f"\n\n<script>\n{js_map}</script>"

def render_template(template_path, context):
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()
    for key, value in context.items():
        html = html.replace(f"{{{{ {key} }}}}", value)
    return html

def main(chapters_dir, title="KBook", repo_url="#"):
    summary_file = os.path.join(chapters_dir, "SUMMARY.md")
    if not os.path.isfile(summary_file):
        print(f"[✗] SUMMARY.md not found in {chapters_dir}")
        sys.exit(1)

    toc_html = parse_summary_to_html(summary_file)

    # Detect default index file
    default_index = ""
    for fname in ["INDEX.md", "index.md"]:
        full_path = os.path.join(chapters_dir, fname)
        if os.path.exists(full_path):
            default_index = fname
            break

    final_html = render_template(TEMPLATE_FILE, {
        "TOC_HTML": toc_html,
        "TITLE_NAME": title,
        "REPO_URL": repo_url,
        "DEFAULT_INDEX": default_index
    })

    with open(os.path.join(chapters_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"[✓] Built {chapters_dir}{OUTPUT_FILE}.")

# Main
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_book.py <chapter-directory>")
        sys.exit(1)

    dir_arg = sys.argv[1]
    if not os.path.isdir(dir_arg):
        print(f"[✗] Error: Directory '{dir_arg}' does not exist.")
        sys.exit(1)

    main(dir_arg)

# EOF
