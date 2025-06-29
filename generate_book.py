import os
import json

CHAPTERS_DIR = "chapters"
TEMPLATE_FILE = "template/index.html"
OUTPUT_FILE = "index.html"

def build_toc():
    toc = []

    for root, _, files in os.walk(CHAPTERS_DIR):
        rel_path = os.path.relpath(root, CHAPTERS_DIR)
        chapter_name = os.path.basename(root)
        children = []

        for file in sorted(files):
            if file.endswith(".md"):
                children.append({
                    "title": file[:-3],
                    "path": os.path.join(rel_path, file).replace("\\", "/")
                })

        if rel_path == ".":
            toc.extend(children)
        else:
            toc.append({
                "title": chapter_name,
                "children": children
            })

    return toc

def render_template(template_path, context):
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    for key, value in context.items():
        placeholder = f"{{{{ {key} }}}}"
        html = html.replace(placeholder, value)

    return html

def main():
    toc = build_toc()
    html = render_template(TEMPLATE_FILE, {
        "TOC_DATA": json.dumps(toc)
    })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[✓] Generated {OUTPUT_FILE} using template.")

if __name__ == "__main__":
    main()

