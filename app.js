const md = window.markdownit({
  html: true,
  highlight: function (str, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return hljs.highlight(str, { language: lang }).value;
      } catch (_) {}
    }
    return '';
  }
});

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
