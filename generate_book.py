import os
import re

OUTPUT_FILE   = "index.html"
SUMMARY_FILE  = "chapters/SUMMARY.md"
TEMPLATE_FILE = "template/index.html"

# Pattern for [Title](path)
link_pattern = re.compile(r"\[\s*(.*?)\s*\]\(\s*(.*?)\s*\)")

def parse_summary_to_html():
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    html_lines = []
    subchapter_refs = []
    chapter_count = 0
    sub_count = 0

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# "):  # Chapter line
            chapter_count += 1
            sub_count = 0
            chapter_title = stripped[2:].strip()
            chapter_id = f"chapter_{chapter_count}"
            escaped_title = chapter_title.replace("'", "\\'").replace('"', '\\"')

            html_lines.append("")  # blank line
            html_lines.append(
                f'        <h3><b><a href="#" onclick="showSubChapters(\'{chapter_id}\', \'{escaped_title}\', \'{chapter_count}\')">{chapter_count}. {chapter_title}</a></b></h3>'
            )
            subchapter_refs.append((chapter_id, []))

        elif match := link_pattern.search(stripped):  # Subchapter
            sub_count += 1
            title, path = match.groups()
            index = f"{chapter_count}.{sub_count}"
            html_lines.append(
                f'        <div style="margin-left:1em;"><a href="#" onclick="loadMarkdown(\'{path}\', \'{escaped_title}\', \'{title}\')">{index}. {title}</a></div>'
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

def main():
    toc_html = parse_summary_to_html()
    final_html = render_template(TEMPLATE_FILE, {
        "TOC_HTML": toc_html
    })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"[✓] Built {OUTPUT_FILE} from SUMMARY.md")

if __name__ == "__main__":
    main()
