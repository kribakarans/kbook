import os
import re

SUMMARY_FILE = "chapters/SUMMARY.md"
TEMPLATE_FILE = "template/index.html"
OUTPUT_FILE = "index.html"

# Pattern for [Title](path.md)
link_pattern = re.compile(r"\[\s*(.*?)\s*\]\(\s*(.*?)\s*\)")

def parse_summary_to_html():
    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    html_lines = []
    chapter_count = 0
    sub_count = 0

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# "):  # Chapter
            chapter_count += 1
            sub_count = 0
            chapter_title = stripped[2:].strip()
            html_lines.append(
                f'<li><b>{chapter_count}. {chapter_title}</b></li>\n'
            )
            html_lines.append("")  # blank line
        elif match := link_pattern.search(stripped):  # Sub-chapter
            sub_count += 1
            title, path = match.groups()
            index = f"{chapter_count}.{sub_count}"
            html_lines.append(
                f'<li style="margin-left:1em;"><a href="#" onclick="loadMarkdown(\'{path}\')"><b>&nbsp;&nbsp;{index}. {title}</b></a></li>\n'
            )
            html_lines.append("")  # blank line
        else:
            continue  # ignore empty lines or bullets without links

    return "\n".join(html_lines)

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
