(function () {
  "use strict";

  var APP_STORE_URL = "https://apps.apple.com/app/id6753987304";
  var APP_REFERRAL_URL = "pythonide://referral";
  var root = document.documentElement;

  function safeStorageGet(key) {
    try { return localStorage.getItem(key); } catch (_) { return null; }
  }

  function safeStorageSet(key, value) {
    try { localStorage.setItem(key, value); } catch (_) {}
  }

  function requestedLanguage() {
    var query = new URLSearchParams(location.search).get("lang");
    if (query === "en" || query === "zh") return query;
    var saved = safeStorageGet("pythonide_site_lang");
    if (saved === "en" || saved === "zh") return saved;
    return /^en\b/i.test(navigator.language || "") ? "en" : "zh";
  }

  function originalText(node) {
    if (node._pythonideZhHTML === undefined && node.querySelector && node.querySelector("br, .title-line")) {
      node._pythonideZhHTML = node.innerHTML;
    }
    if (!node.dataset.zh) node.dataset.zh = node.textContent.trim();
    return node.dataset.zh;
  }

  function setMeta(selector, lang) {
    var node = document.querySelector(selector);
    if (!node) return;
    var value = lang === "en" ? node.dataset.en : node.dataset.zh;
    if (!value) return;
    if (node.tagName === "TITLE") node.textContent = value;
    else node.setAttribute("content", value);
  }

  function setLanguage(lang, updateURL) {
    lang = lang === "en" ? "en" : "zh";
    root.lang = lang === "en" ? "en" : "zh-CN";
    root.dataset.lang = lang;
    safeStorageSet("pythonide_site_lang", lang);

    document.querySelectorAll("[data-en]").forEach(function (node) {
      if (node.matches("meta, title")) return;
      var zh = originalText(node);
      if (lang === "en") node.textContent = node.dataset.en;
      else if (node._pythonideZhHTML !== undefined) node.innerHTML = node._pythonideZhHTML;
      else node.textContent = zh;
    });
    document.querySelectorAll("[data-lang]").forEach(function (button) {
      button.setAttribute("aria-pressed", button.dataset.lang === lang ? "true" : "false");
    });
    document.querySelectorAll("[data-label-en]").forEach(function (node) {
      if (!node.dataset.labelZh) node.dataset.labelZh = node.getAttribute("aria-label") || "";
      node.setAttribute("aria-label", lang === "en" ? node.dataset.labelEn : node.dataset.labelZh);
    });
    document.querySelectorAll("[data-alt-en]").forEach(function (node) {
      if (!node.dataset.altZh) node.dataset.altZh = node.getAttribute("alt") || "";
      node.setAttribute("alt", lang === "en" ? node.dataset.altEn : node.dataset.altZh);
    });

    setMeta("title[data-zh]", lang);
    setMeta('meta[name="description"][data-zh]', lang);
    setMeta('meta[property="og:title"][data-zh]', lang);
    setMeta('meta[property="og:description"][data-zh]', lang);
    setMeta('meta[name="twitter:title"][data-zh]', lang);
    setMeta('meta[name="twitter:description"][data-zh]', lang);

    if (updateURL) {
      var url = new URL(location.href);
      if (lang === "en") url.searchParams.set("lang", "en");
      else url.searchParams.delete("lang");
      history.replaceState({}, "", url.pathname + url.search + url.hash);
      updateCanonical(url);
    }
    document.dispatchEvent(new CustomEvent("pythonide:language", { detail: { lang: lang } }));
  }

  var languageChangeToken = 0;

  function visibleLanguageTargets() {
    var nodes = Array.prototype.slice.call(document.querySelectorAll(".site-header [data-en], main [data-en], .site-footer [data-en], [data-app-modal]:not([hidden]) [data-en]"));
    return nodes.filter(function (node) {
      if (node.matches("meta, title, .language-toggle, .language-toggle *")) return false;
      if (nodes.some(function (parent) { return parent !== node && parent.contains(node); })) return false;
      var rect = node.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0 && rect.bottom > -40 && rect.top < innerHeight + 40;
    });
  }

  function transitionLanguage(lang) {
    lang = lang === "en" ? "en" : "zh";
    if (root.dataset.lang === lang) return;
    if (matchMedia("(prefers-reduced-motion: reduce)").matches || !Element.prototype.animate) {
      setLanguage(lang, true);
      return;
    }

    var token = ++languageChangeToken;
    var targets = visibleLanguageTargets();
    root.classList.add("is-language-switching");
    root.dataset.lang = lang;
    document.querySelectorAll("[data-lang]").forEach(function (button) {
      button.setAttribute("aria-pressed", button.dataset.lang === lang ? "true" : "false");
    });

    var leaving = targets.map(function (node, index) {
      return node.animate([
        { opacity: 1, transform: "translateY(0)", filter: "blur(0)" },
        { opacity: 0, transform: "translateY(-4px)", filter: "blur(1.5px)" }
      ], { duration: 105 + Math.min(index, 5) * 8, easing: "cubic-bezier(.4,0,1,1)", fill: "forwards" });
    });

    Promise.all(leaving.map(function (animation) { return animation.finished.catch(function () {}); })).then(function () {
      if (token !== languageChangeToken) return;
      setLanguage(lang, true);
      leaving.forEach(function (animation) { animation.cancel(); });
      targets.forEach(function (node, index) {
        node.animate([
          { opacity: 0, transform: "translateY(5px)", filter: "blur(1.5px)" },
          { opacity: 1, transform: "translateY(0)", filter: "blur(0)" }
        ], { duration: 220 + Math.min(index, 6) * 10, delay: Math.min(index, 6) * 8, easing: "cubic-bezier(.22,1,.36,1)" });
      });
      setTimeout(function () {
        if (token === languageChangeToken) root.classList.remove("is-language-switching");
      }, 330);
    });
  }

  function resolvedTheme() {
    var saved = safeStorageGet("pythonide_site_theme");
    if (saved === "light" || saved === "dark") return saved;
    return matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyTheme(theme, persist) {
    theme = theme === "dark" ? "dark" : "light";
    root.dataset.theme = theme;
    if (persist) safeStorageSet("pythonide_site_theme", theme);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.content = theme === "dark" ? "#171717" : "#ffffff";
    document.querySelectorAll("[data-theme-toggle]").forEach(function (button) {
      var label = theme === "dark" ? "切换到浅色 / Switch to light" : "切换到深色 / Switch to dark";
      button.setAttribute("aria-label", label);
      button.setAttribute("title", label);
      button.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
    });
  }

  function setupThemeControls() {
    document.querySelectorAll("[data-theme-toggle]").forEach(function (button) {
      button.innerHTML = '<svg class="theme-icon theme-icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3 7 7 0 0 0 21 12.8Z"/></svg><svg class="theme-icon theme-icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/><path d="M12 2.5V5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M18.7 5.3l-1.8 1.8M7.1 16.9l-1.8 1.8"/></svg>';
    });
    var themeQuery = matchMedia("(prefers-color-scheme: dark)");
    if (themeQuery.addEventListener) {
      themeQuery.addEventListener("change", function (event) {
        if (!safeStorageGet("pythonide_site_theme")) applyTheme(event.matches ? "dark" : "light", false);
      });
    }
  }

  function setupLanguageControls() {
    document.querySelectorAll(".language-toggle").forEach(function (group) {
      group.setAttribute("role", "group");
      if (!group.getAttribute("aria-label")) group.setAttribute("aria-label", "语言 / Language");
    });
  }

  function setupMenuControls() {
    document.querySelectorAll("[data-menu-toggle]").forEach(function (button) {
      button.innerHTML = '<span class="menu-glyph" aria-hidden="true"><span class="menu-line"></span><span class="menu-line"></span><span class="menu-line"></span></span>';
    });
  }

  function updateCanonical(url) {
    var canonical = document.querySelector('link[rel="canonical"]');
    var ogURL = document.querySelector('meta[property="og:url"]');
    if (!canonical) return;
    var normalized = new URL(canonical.href);
    if (url.searchParams.get("lang") === "en") normalized.searchParams.set("lang", "en");
    else normalized.searchParams.delete("lang");
    canonical.href = normalized.href;
    if (ogURL) ogURL.content = normalized.href;
  }

  function setupNavigation() {
    var menu = document.querySelector("[data-nav-links]");
    var toggle = document.querySelector("[data-menu-toggle]");
    if (!menu || !toggle) return;
    var backdrop = document.querySelector("[data-nav-backdrop]");
    if (!backdrop) {
      backdrop = document.createElement("button");
      backdrop.type = "button";
      backdrop.className = "nav-backdrop";
      backdrop.dataset.navBackdrop = "";
      backdrop.tabIndex = -1;
      backdrop.setAttribute("aria-hidden", "true");
      document.body.appendChild(backdrop);
    }
    function updateToggleLabel(open) {
      var english = root.dataset.lang === "en";
      var label = open ? (english ? "Close navigation menu" : "关闭导航菜单") : (english ? "Open navigation menu" : "打开导航菜单");
      toggle.setAttribute("aria-label", label);
      toggle.setAttribute("title", label);
    }
    function close(restoreFocus) {
      menu.dataset.open = "false";
      toggle.setAttribute("aria-expanded", "false");
      document.body.classList.remove("nav-is-open");
      updateToggleLabel(false);
      if (restoreFocus) toggle.focus();
    }
    toggle.addEventListener("click", function () {
      var open = menu.dataset.open !== "true";
      menu.dataset.open = open ? "true" : "false";
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.classList.toggle("nav-is-open", open);
      updateToggleLabel(open);
    });
    backdrop.addEventListener("click", function () { close(true); });
    menu.querySelectorAll("a").forEach(function (link) { link.addEventListener("click", function () { close(false); }); });
    document.addEventListener("click", function (event) {
      if (menu.dataset.open === "true" && !menu.contains(event.target) && !toggle.contains(event.target) && event.target !== backdrop) close(false);
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && menu.dataset.open === "true") {
        close(true);
      }
    });
    document.addEventListener("pythonide:language", function () { updateToggleLabel(menu.dataset.open === "true"); });
    addEventListener("resize", function () { if (innerWidth > 780) close(false); }, { passive: true });
    updateToggleLabel(false);
  }

  function setupGlobalNavigationExtras() {
    document.querySelectorAll("[data-nav-links]").forEach(function (menu) {
      if (menu.querySelector('.nav-external[href*="github.com/Python-IDE/PythonIDE-iOS"]')) return;
      var download = menu.querySelector(".nav-download");
      if (!download) return;
      var github = document.createElement("a");
      github.className = "nav-link nav-external";
      github.href = "https://github.com/Python-IDE/PythonIDE-iOS";
      github.target = "_blank";
      github.rel = "noreferrer";
      github.textContent = "GitHub";
      menu.insertBefore(github, download);
    });
  }

  function setupNavigationIndicator() {
    document.querySelectorAll("[data-nav-links]").forEach(function (menu) {
      var active = menu.querySelector('.nav-link[aria-current="page"]');
      if (!active) return;
      var pill = document.createElement("span");
      pill.className = "nav-active-pill";
      pill.setAttribute("aria-hidden", "true");
      menu.insertBefore(pill, menu.firstChild);
      menu.classList.add("has-active-pill");

      function moveTo(link) {
        if (!link || innerWidth <= 780) return;
        pill.style.setProperty("--pill-x", link.offsetLeft + "px");
        pill.style.setProperty("--pill-width", link.offsetWidth + "px");
      }
      moveTo(active);
      menu.querySelectorAll(".nav-link").forEach(function (link) {
        link.addEventListener("mouseenter", function () { moveTo(link); });
        link.addEventListener("focus", function () { moveTo(link); });
      });
      menu.addEventListener("mouseleave", function () { moveTo(active); });
      menu.addEventListener("focusout", function (event) { if (!menu.contains(event.relatedTarget)) moveTo(active); });
      document.addEventListener("pythonide:language", function () { requestAnimationFrame(function () { moveTo(active); }); });
      addEventListener("resize", function () { moveTo(active); }, { passive: true });
    });
  }

  function setupHeaderFeedback() {
    var header = document.querySelector(".site-header");
    if (!header) return;
    var sync = function () { header.classList.toggle("is-scrolled", scrollY > 8); };
    sync();
    addEventListener("scroll", sync, { passive: true });
  }

  function copyText(value) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(value);
    return new Promise(function (resolve, reject) {
      var area = document.createElement("textarea");
      area.value = value;
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.left = "-9999px";
      document.body.appendChild(area);
      area.select();
      try { document.execCommand("copy") ? resolve() : reject(new Error("copy")); }
      catch (error) { reject(error); }
      area.remove();
    });
  }

  function toast(zh, en) {
    var node = document.querySelector("[data-toast]");
    if (!node) {
      node = document.createElement("div");
      node.className = "toast";
      node.dataset.toast = "";
      document.body.appendChild(node);
    }
    node.textContent = root.dataset.lang === "en" ? (en || zh) : zh;
    node.classList.add("show");
    clearTimeout(toast.timer);
    toast.timer = setTimeout(function () { node.classList.remove("show"); }, 1800);
  }

  function setupCopy() {
    document.querySelectorAll("[data-copy]").forEach(function (button) {
      button.addEventListener("click", function () {
        var value = button.dataset.copy || location.href;
        copyText(value).then(function () {
          toast(button.dataset.successZh || "已复制", button.dataset.successEn || "Copied");
        }).catch(function () {
          toast("复制失败，请手动复制", "Copy failed. Please copy manually.");
        });
      });
    });
  }

  function inviteCode() {
    var url = new URL(location.href);
    var raw = url.searchParams.get("code") || "";
    var match = location.pathname.match(/^\/i\/([A-Za-z0-9-]+)/);
    if (!raw && match) raw = match[1];
    var normalized = raw.replace(/[\s-]+/g, "").toUpperCase();
    return /^[A-Z0-9]{4,12}$/.test(normalized) ? normalized : "";
  }

  function setupInvite() {
    var codeNode = document.querySelector("[data-invite-code]");
    if (!codeNode) return;
    var code = inviteCode();
    var copyButton = document.querySelector("[data-copy-invite]");
    var title = document.querySelector("[data-invite-title]");
    var summary = document.querySelector("[data-invite-summary]");
    if (code) {
      codeNode.textContent = code;
      codeNode.classList.remove("is-empty");
      if (copyButton) { copyButton.hidden = false; copyButton.dataset.copy = code; }
      if (title) { title.dataset.zh = "好友邀请你使用 PythonIDE"; title.dataset.en = "A friend invited you to PythonIDE"; }
      if (summary) { summary.dataset.zh = "下载 App 后输入邀请码，即可建立邀请关系。"; summary.dataset.en = "Download the app and enter this code to connect the referral."; }
      var localizedTitleNodes = document.querySelectorAll('title, meta[property="og:title"], meta[name="twitter:title"]');
      localizedTitleNodes.forEach(function (node) {
        node.dataset.zh = "使用邀请码 " + code + " 加入 PythonIDE";
        node.dataset.en = "Join PythonIDE with invite code " + code;
      });
      var canonical = document.querySelector('link[rel="canonical"]');
      if (canonical) {
        var canonicalURL = new URL("https://pythonide.xin/i/");
        canonicalURL.searchParams.set("code", code);
        if (root.dataset.lang === "en") canonicalURL.searchParams.set("lang", "en");
        canonical.href = canonicalURL.href;
        var ogURL = document.querySelector('meta[property="og:url"]');
        if (ogURL) ogURL.content = canonicalURL.href;
      }
    } else {
      codeNode.textContent = root.dataset.lang === "en" ? "Get your code" : "获取邀请码";
      codeNode.classList.add("is-empty");
      if (copyButton) copyButton.hidden = true;
    }
    setLanguage(root.dataset.lang || requestedLanguage(), false);
  }

  function openInApp() {
    var modal = document.querySelector("[data-app-modal]");
    if (modal) modal._pythonideReturnFocus = document.activeElement;
    var hidden = false;
    var onVisibility = function () { if (document.hidden) hidden = true; };
    document.addEventListener("visibilitychange", onVisibility, { once: true });
    location.href = APP_REFERRAL_URL;
    setTimeout(function () {
      document.removeEventListener("visibilitychange", onVisibility);
      if (!hidden && modal) {
        modal.hidden = false;
        document.body.style.overflow = "hidden";
        var first = modal.querySelector("button, a");
        if (first) first.focus();
      }
    }, 1050);
  }

  function setupAppOpen() {
    document.querySelectorAll("[data-open-app]").forEach(function (button) { button.addEventListener("click", openInApp); });
    var modal = document.querySelector("[data-app-modal]");
    if (!modal) return;
    function close() {
      modal.hidden = true;
      document.body.style.overflow = "";
      if (modal._pythonideReturnFocus && modal._pythonideReturnFocus.focus) modal._pythonideReturnFocus.focus();
    }
    modal.querySelectorAll("[data-modal-close]").forEach(function (button) { button.addEventListener("click", close); });
    modal.addEventListener("click", function (event) { if (event.target === modal) close(); });
    document.addEventListener("keydown", function (event) {
      if (modal.hidden) return;
      if (event.key === "Escape") { close(); return; }
      if (event.key !== "Tab") return;
      var focusable = Array.prototype.slice.call(modal.querySelectorAll('button:not([disabled]), a[href], [tabindex]:not([tabindex="-1"])'));
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
      else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
    });
  }

  function init() {
    root.classList.add("motion-ready");
    setupThemeControls();
    setupLanguageControls();
    setupMenuControls();
    applyTheme(resolvedTheme(), false);
    setLanguage(requestedLanguage(), false);
    updateCanonical(new URL(location.href));
    setupGlobalNavigationExtras();
    setupNavigationIndicator();
    setupNavigation();
    setupHeaderFeedback();
    setupCopy();
    setupInvite();
    setupAppOpen();

    document.querySelectorAll("[data-download]").forEach(function (link) { link.href = APP_STORE_URL; });
    document.querySelectorAll("[data-lang]").forEach(function (button) {
      button.addEventListener("click", function () { transitionLanguage(button.dataset.lang); });
    });
    document.querySelectorAll("[data-theme-toggle]").forEach(function (button) {
      button.addEventListener("click", function () { applyTheme(root.dataset.theme === "dark" ? "light" : "dark", true); });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
}());
