const md = window.markdownit({
  html: true,
  highlight: (str, lang) => {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return hljs.highlight(str, { language: lang }).value;
      } catch (_) {}
    }
    return ''; 
  }
});

function createToc(toc, parent) {
  toc.forEach(item => {
    const li = document.createElement("li");
    if (item.children) {
      const details = document.createElement("details");
      const summary = document.createElement("summary");
      summary.textContent = item.title;
      details.appendChild(summary);
      const subList = document.createElement("ul");
      createToc(item.children, subList);
      details.appendChild(subList);
      li.appendChild(details);
    } else {
      const a = document.createElement("a");
      a.href = "#";
      a.textContent = item.title;
      a.onclick = () => loadMarkdown(item.path);
      li.appendChild(a);
    }
    parent.appendChild(li);
  });
}

function loadMarkdown(path) {
  fetch("chapters/" + path)
    .then(res => res.text())
    .then(mdText => {
      const html = md.render(mdText);
      document.getElementById("content").innerHTML = html;
      hljs.highlightAll();
    })
    .catch(err => {
      document.getElementById("content").innerHTML = "<p>Error loading file.</p>";
      console.error(err);
    });
}

window.addEventListener("DOMContentLoaded", () => {
  const tocList = document.getElementById("toc");
  createToc(TOC_DATA, tocList);
});

