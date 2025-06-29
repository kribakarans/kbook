import os
import re
import json

SUMMARY_FILE = "chapters/SUMMARY.md"
TEMPLATE_FILE = "template/index.html"
OUTPUT_FILE = "index.html"

link_pattern = re.compile(r'\[\s*(.*?)\s*\]\(\s*(.*?)\s*\)')

def parse_summary(lines):
    toc = []
    stack = [(-1, toc)]  # (indent_level, children)

    for line in lines:
        indent = len(line) - len(line.lstrip(" "))
        match = link_pattern.search(line)
        node = None

        if match:
            title, path = match.groups()
            node = {"title": title, "path": path}
        else:
            stripped = line.strip()
            if stripped.startswith("- "):
                title = stripped[2:]
                node = {"title": title, "children": []}

        if node:
            while stack and stack[-1][0] >= indent:
                stack.pop()
            parent = stack[-1][1]
            if "children" in node:
                parent.append(node)
                stack.append((indent, node["children"]))
            else:
                parent.append(node)

    return toc

def render_template(template_path, context):
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()
    for key, value in context.items():
        html = html.replace(f"{{{{ {key} }}}}", value)
    return html

def main():
    if not os.path.exists(SUMMARY_FILE):
        print("ERROR: SUMMARY.md not found.")
        return

    with open(SUMMARY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    toc = parse_summary(lines)
    html = render_template(TEMPLATE_FILE, {
        "TOC_DATA": json.dumps(toc)
    })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[✓] Built {OUTPUT_FILE} from SUMMARY.md.")

if __name__ == "__main__":
    main()

