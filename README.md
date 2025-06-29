# KBook: MD Book Generator

A lightweight `mdBook`-like static site generator to view and browse Markdown-based books with a sidebar.

- Sidebar with chapters & subchapters from `SUMMARY.md`
- Clickable **chapter headers** show their subchapters in preview
- Clickable **subchapters** load the actual Markdown content
- GitHub dark theme & syntax highlighting via `highlight.js`

## Directory Structure

```
project/
├── chapters/               # Your markdown content here
│   ├── SUMMARY.md          # Defines chapter structure
│   ├── intro.md
│   └── getting-started.md
├── template/
│   └── index.html          # HTML template with placeholder
├── style.css               # UI styling
├── app.js                  # JS to load and render markdown
├── generate_book.py        # Python script to build final HTML
└── index.html              # Output generated file
```

## How It Works

- `generate_book.py` reads your `chapters/SUMMARY.md`
- It builds a sidebar with numbered chapters (`#`) and subchapters (`- [Title](file.md)`)
- On chapter click → preview shows list of subchapters
- On subchapter click → loads and renders the Markdown with `markdown-it`

## Writing `SUMMARY.md`

```md
# Introduction

- [Welcome](intro.md)
- [Setup](setup.md)

# Getting Started

- [Basics](getting-started.md)
- [Examples](examples.md)
```

- `# Heading` is a top-level chapter
- `- [Title](file.md)` are subchapters inside the chapter

## Getting Started

1. Clone or download the repo

2. Place your markdown files in chapters/ and structure them using chapters/SUMMARY.md

3. Generate the final HTML

	python generate_book.py

4. Open it in browser

	xdg-open index.html  # or open index.html manually

## Features

| Feature                  | Description                                |
|--------------------------|--------------------------------------------|
| Static output            | Generates `index.html` without a webserver |
| GitHub dark theme        | via `github-markdown-dark.css`             |
| Syntax highlighting      | via `highlight.js`                         |
| No dependencies          | Just Python 3, JS, HTML                    |

## Dependencies

Only needs Python 3 to generate the HTML.

In the browser:
- [markdown-it](https://github.com/markdown-it/markdown-it)
- [highlight.js](https://highlightjs.org/)
- [GitHub markdown CSS](https://github.com/sindresorhus/github-markdown-css)

