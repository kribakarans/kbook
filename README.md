# KBook: MD Book Generator

A lightweight `mdBook`-like static site generator to view and browse Markdown-based books.

## Features

| Feature                   | Description                                               |
|---------------------------|-----------------------------------------------------------|
| Title & Repo support      | Page title and repo link from command-line args           |
| Sidebar navigation        | Auto-generated from `SUMMARY.md`                          |
| Chapter preview           | Clicking chapter shows its subchapters                    |
| Live content loading      | Subchapters load via JavaScript (Markdown + code support) |
| GitHub dark theme         | Beautiful styling using `github-markdown-css`             |
| Syntax highlighting       | With `highlight.js` for all major languages               |
| Render all file           | Additionaly render all file types                         |
| Mobile-friendly           | Responsive layout for phones/tablets                      |

## Directory Structure

```
kbook/
├── Makefile
├── README.md
├── share
│   └── index.html.in
└── src
    ├── build_summary.py
    ├── generate_book.py
    └── kbook.py
```

## How It Works

- `kbook.py` is the main entry point.
- `build_summary.py` optionally auto-generates `SUMMARY.md` from folder structure.
- `generate_book.py` parses `SUMMARY.md` and populates the TOC.
- `index.html` is built from a template and dynamic TOC.
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
```bash
git clone git@github.com:kribakarans/kbook.git
cd kbook && make install
```

2. Go to the repo you want to build as a MD-Book, and run the `kbook` CLI:

Example:
```bash
cd howto/

howto/
└── topics
    ├── chroot
    ├── docker
    ├── gitweb
    ├── redmine
    └── whatsapp
```

3. Generate the final HTML
```
kbook <title> <chapter-dir> <repo-url>
```
Example:
```
kbook "Howto" topics/ https://github.com/kribakarans/howo/
```
4. Run web server and visit http://localhost:1111/
```
python -m http.server 1111
```
## Dependencies

In the browser:
- Python 3
- [markdown-it](https://github.com/markdown-it/markdown-it)
- [highlight.js](https://highlightjs.org/)
- [GitHub markdown CSS](https://github.com/sindresorhus/github-markdown-css)

---
