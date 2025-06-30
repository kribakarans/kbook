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

function showSubChapters(chapterId, chapterTitle, chapterNum) {
  const subchapters = window.chapterMap?.[chapterId];
  const content = document.getElementById("content");
  const chapterHeader = document.getElementById("chapter-title");
  const chapterSource = document.getElementById("chapter-source");

  chapterSource.textContent = "";
  chapterHeader.textContent = `${chapterNum}. ${chapterTitle}`;

  let html = "";
  if (!subchapters || subchapters.length === 0) {
    html += `<p>No subchapters found.</p>`;
  } else {
    html += "<ul>";
    for (const item of subchapters) {
      html += `<li><a href="#" onclick="loadMarkdown('${item.path}')">${item.index}. ${item.title}</a></li>`;
    }
    html += "</ul>";
  }

  content.innerHTML = html;
}

function loadMarkdown(path, chapterTitle, subTitle) {
  const header = `${chapterTitle}/${subTitle}`;
  const ext = path.split('.').pop().toLowerCase();
  const content = document.getElementById("content");
  const chapterHeader = document.getElementById("chapter-title");
  const chapterSource = document.getElementById("chapter-source");

  chapterSource.textContent = `${path}`;
  chapterHeader.textContent = `${header}`;

  fetch("chapters/" + path)
    .then(res => res.text())
    .then(data => {
      if (ext === 'md') {
        content.innerHTML = md.render(data);
      } else {
        const langMap = {
          'c': 'c',
          'cpp': 'cpp',
          'py': 'python',
          'js': 'javascript',
          'html': 'html',
          'json': 'json',
          'java': 'java',
          'sh': 'bash'
        };
        const lang = langMap[ext] || '';
        const codeBlock = `<pre><code class="language-${lang}">${escapeHtml(data)}</code></pre>`;
        content.innerHTML = codeBlock;
        hljs.highlightAll();
      }
    })
    .catch(err => {
      content.innerHTML = "<p>Error loading file.</p>";
      console.error(err);
    });
}

function escapeHtml(str) {
  return str.replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");
}
