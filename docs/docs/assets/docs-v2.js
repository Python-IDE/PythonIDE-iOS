(() => {
  const root = document.documentElement;
  const savedTheme = localStorage.getItem("docs-v2-theme");
  if (savedTheme) root.dataset.theme = savedTheme;

  const prefix = window.PYTHONIDE_DOCS_PREFIX || "";
  const themeToggle = document.querySelector(".theme-toggle");
  themeToggle?.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    localStorage.setItem("docs-v2-theme", next);
  });

  const menuToggle = document.querySelector(".menu-toggle");
  const backdrop = document.querySelector(".mobile-backdrop");
  const languageMenu = document.querySelector(".language-menu");
  const closeSidebar = () => document.body.classList.remove("sidebar-open");
  menuToggle?.addEventListener("click", () => document.body.classList.toggle("sidebar-open"));
  backdrop?.addEventListener("click", closeSidebar);
  document.querySelectorAll(".nav-link").forEach((link) => link.addEventListener("click", closeSidebar));
  document.addEventListener("click", (event) => {
    if (languageMenu && !languageMenu.contains(event.target)) {
      languageMenu.open = false;
    }
  });

  document.querySelectorAll(".copy-code").forEach((button) => {
    button.addEventListener("click", async () => {
      const id = button.getAttribute("data-copy-code");
      const code = document.getElementById(`code-${id}`)?.textContent || "";
      await navigator.clipboard.writeText(code);
      const old = button.textContent;
      button.textContent = "已复制";
      setTimeout(() => { button.textContent = old; }, 1200);
    });
  });

  highlightCodeBlocks();

  const tocLinks = [...document.querySelectorAll(".toc-link")];
  const headings = tocLinks
    .map((link) => document.getElementById(decodeURIComponent((link.getAttribute("href") || "").slice(1))))
    .filter(Boolean);
  if (headings.length) {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      tocLinks.forEach((link) => link.classList.toggle("active", link.getAttribute("href") === `#${visible.target.id}`));
    }, { rootMargin: "-20% 0px -70% 0px", threshold: [0, 1] });
    headings.forEach((heading) => observer.observe(heading));
  }

  const panel = document.querySelector(".search-panel");
  const input = document.getElementById("docs-search-input");
  const results = document.getElementById("docs-search-results");
  let searchIndex = [];
  let loaded = false;

  async function loadSearch() {
    if (loaded) return;
    loaded = true;
    try {
      const response = await fetch(`${prefix}search-index.json`);
      searchIndex = await response.json();
    } catch {
      searchIndex = [];
    }
  }

  async function openSearch() {
    await loadSearch();
    panel?.classList.add("open");
    input?.focus();
    renderSearch("");
  }

  function closeSearch() {
    panel?.classList.remove("open");
  }

  function renderSearch(query) {
    if (!results) return;
    const q = query.trim().toLowerCase();
    const tokens = q.split(/[\s,，。;；:：/|()[\]{}"'`]+/).filter(Boolean);
    const matches = q.length === 0
      ? searchIndex.slice(0, 12)
      : searchIndex
          .map((item) => {
            const title = item.title.toLowerCase();
            const subtitle = (item.subtitle || "").toLowerCase();
            const section = item.section.toLowerCase();
            const text = item.text.toLowerCase();
            let score = text.includes(q) ? 80 : 0;
            for (const token of tokens) {
              if (title.includes(token)) score += 40;
              else if (subtitle.includes(token)) score += 18;
              else if (section.includes(token)) score += 12;
              else if (text.includes(token)) score += 6;
            }
            return { item, score };
          })
          .filter((entry) => entry.score > 0)
          .sort((a, b) => b.score - a.score || a.item.title.localeCompare(b.item.title))
          .slice(0, 24)
          .map((entry) => entry.item);
    results.innerHTML = matches.map((item) => `
      <a class="search-result" href="${prefix}${item.url}">
        <strong>${escapeHtml(item.title)}</strong>
        <span>${escapeHtml(item.section)} · ${escapeHtml(item.subtitle || "")}</span>
      </a>
    `).join("") || '<div class="search-result"><strong>没有结果</strong><span>换一个 API、模块或关键词试试。</span></div>';
  }

  function escapeHtml(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function highlightCodeBlocks() {
    document.querySelectorAll("pre code").forEach((code) => {
      if (code.dataset.highlighted === "true") return;
      code.innerHTML = highlightCode(code.textContent || "");
      code.dataset.highlighted = "true";
    });
  }

  function highlightCode(source) {
    const keywords = new Set([
      "and", "as", "async", "await", "break", "case", "catch", "class", "const",
      "continue", "def", "elif", "else", "except", "false", "False", "finally",
      "for", "from", "function", "if", "import", "in", "is", "let", "nil", "None",
      "not", "null", "or", "pass", "return", "switch", "throw", "true", "True",
      "try", "var", "while", "with", "yield"
    ]);
    const tokenPattern = /(?:\"\"\"[\s\S]*?\"\"\"|'''[\s\S]*?'''|`(?:\\[\s\S]|[^`\\])*`|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\/\*[\s\S]*?\*\/|\/\/[^\n]*|#[^\n]*|\.[A-Za-z_]\w*|\b\d+(?:\.\d+)?\b|\b[A-Za-z_]\w*\b)/g;
    let html = "";
    let lastIndex = 0;
    let match;
    while ((match = tokenPattern.exec(source)) !== null) {
      const token = match[0];
      const index = match.index;
      html += escapeHtml(source.slice(lastIndex, index));
      html += renderToken(token, source, index, keywords);
      lastIndex = index + token.length;
    }
    return html + escapeHtml(source.slice(lastIndex));
  }

  function renderToken(token, source, index, keywords) {
    const escaped = escapeHtml(token);
    if (token.startsWith("//") || token.startsWith("#") || token.startsWith("/*")) {
      return `<span class="tok-comment">${escaped}</span>`;
    }
    if (token.startsWith('"') || token.startsWith("'") || token.startsWith("`")) {
      return `<span class="tok-string">${escaped}</span>`;
    }
    if (/^\d/.test(token)) {
      return `<span class="tok-number">${escaped}</span>`;
    }
    if (token.startsWith(".")) {
      return `.<span class="tok-property">${escapeHtml(token.slice(1))}</span>`;
    }
    if (keywords.has(token)) {
      return `<span class="tok-keyword">${escaped}</span>`;
    }
    const after = source.slice(index + token.length).match(/^\s*/)?.[0] || "";
    if (source[index + token.length + after.length] === "(") {
      return `<span class="tok-function">${escaped}</span>`;
    }
    return escaped;
  }

  document.querySelector(".search-trigger")?.addEventListener("click", openSearch);
  document.querySelector(".search-close")?.addEventListener("click", closeSearch);
  panel?.addEventListener("click", (event) => {
    if (event.target === panel) closeSearch();
  });
  input?.addEventListener("input", () => renderSearch(input.value));
  window.addEventListener("keydown", (event) => {
    if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
      event.preventDefault();
      openSearch();
    } else if (event.key === "Escape") {
      closeSearch();
    }
  });
})();
