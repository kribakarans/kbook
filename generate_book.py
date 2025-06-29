import os
import json

CHAPTERS_DIR = "chapters"
OUTPUT_FILE = "index.html"

def build_toc():
    toc = []

    for root, dirs, files in os.walk(CHAPTERS_DIR):
        rel_path = os.path.relpath(root, CHAPTERS_DIR)
        chapter_name = os.path.basename(root)
        if rel_path == ".":
            chapter_name = "Home"
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

def generate_index_html(toc):
    with open("index.html", "w") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>My Markdown Book</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.5.1/github-markdown-dark.min.css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div id="container">
  <nav id="sidebar">
    <h2>📘 Chapters</h2>
    <ul id="toc"></ul>
  </nav>
  <main id="content" class="markdown-body">
    <h2>Welcome</h2>
    <p>Select a chapter from the sidebar to begin reading.</p>
  </main>
</div>
<script>
  const TOC_DATA = {json.dumps(toc)};
</script>
<script src="https://cdn.jsdelivr.net/npm/markdown-it@13.0.1/dist/markdown-it.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="app.js"></script>
</body>
</html>
""")

def main():
    toc = build_toc()
    generate_index_html(toc)
    print(f"[✓] Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

