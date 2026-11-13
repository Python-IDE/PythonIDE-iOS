(function () {
  "use strict";

  const root = document.querySelector("[data-showcase]");
  const feedURL = new URL(root.dataset.feed);
  const form = root.querySelector("[data-showcase-search]");
  const search = form.elements.q;
  const list = root.querySelector("[data-showcase-list]");
  const statusLines = [...root.querySelectorAll("[data-showcase-status] [data-state]")];
  const latest = root.querySelector("[data-showcase-latest]");
  const results = root.querySelector("[data-showcase-results]");
  const more = root.querySelector("[data-showcase-more]");
  const retry = root.querySelector("[data-showcase-retry]");
  const template = document.getElementById("showcase-site");
  const pageSize = 24;
  const requestTimeoutMS = 10_000;
  const displayed = new Set();
  let query = "";
  let nextCursor = null;
  let request;

  function normalizedText(value, maximum) {
    return typeof value === "string" ? value.trim().slice(0, maximum) : "";
  }

  function httpsURL(value) {
    if (typeof value !== "string" || value.length > 2048) return null;
    try {
      const url = new URL(value);
      return url.protocol === "https:" && !url.username && !url.password && !url.port ? url : null;
    } catch {
      return null;
    }
  }

  function imageWhenReady(container, url, image) {
    image.addEventListener("load", () => { container.dataset.imageReady = ""; }, { once: true });
    image.addEventListener("error", () => { image.remove(); }, { once: true });
    image.src = url.href;
    container.append(image);
  }

  function coverLabel(node) {
    node.textContent = document.documentElement.lang === "en" ? node.dataset.en : "打开网站";
  }

  function publicProfileURL(value) {
    const url = httpsURL(value);
    if (url?.origin !== "https://link.pythonide.xin" || url.search || url.hash) return null;
    const match = /^\/community\/user\/([^/]+)$/.exec(url.pathname);
    if (!match) return null;
    try {
      const id = decodeURIComponent(match[1]);
      return /^[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$/.test(id) ? url : null;
    } catch {
      return null;
    }
  }

  function authorRow(author) {
    const name = normalizedText(author?.name, 80);
    if (!name) return null;
    const profile = publicProfileURL(author.profileUrl);
    const row = document.createElement(profile ? "a" : "div");
    row.className = "showcase-author";
    if (profile) {
      row.href = profile.href;
      row.rel = "noreferrer";
    }

    const avatar = document.createElement("span");
    avatar.className = "showcase-avatar";
    avatar.setAttribute("aria-hidden", "true");
    const initial = document.createElement("span");
    initial.textContent = Array.from(name)[0];
    avatar.append(initial);
    if (typeof author.avatarId === "string" && /^avatar_(?!0000)[0-9]{4}$/.test(author.avatarId)) {
      const avatarURL = new URL("https://api.dicebear.com/9.x/adventurer/png");
      avatarURL.search = new URLSearchParams({ seed: author.avatarId, size: "160" });
      const image = new Image(28, 28);
      image.alt = "";
      image.loading = "lazy";
      image.decoding = "async";
      image.referrerPolicy = "no-referrer";
      imageWhenReady(avatar, avatarURL, image);
    }

    const label = document.createElement("span");
    label.className = "showcase-author-name";
    label.dir = "auto";
    label.textContent = name;
    label.title = name;
    row.append(avatar, label);
    return row;
  }

  function siteCard(site, url) {
    const domain = url.hostname + (url.pathname === "/" ? "" : url.pathname.replace(/\/$/, ""));
    const name = normalizedText(site.name, 80) || domain;
    const item = template.content.firstElementChild.cloneNode(true);
    const link = item.querySelector("[data-site-link]");
    link.href = url.href;
    link.rel = "noreferrer";
    const title = item.querySelector("[data-site-name]");
    title.textContent = name;
    title.title = name;
    const address = item.querySelector("[data-site-domain]");
    address.textContent = domain;
    address.title = domain;
    coverLabel(item.querySelector(".showcase-cover-placeholder span"));

    const coverURL = httpsURL(site.thumbnailUrl);
    if (coverURL && [feedURL.origin, "https://pythonide.xin"].includes(coverURL.origin)) {
      const cover = item.querySelector(".showcase-cover");
      imageWhenReady(cover, coverURL, cover.querySelector("img"));
    }

    const author = authorRow(site.author);
    if (author) item.append(author);
    return item;
  }

  function readPage(data, cursor) {
    const next = data?.nextCursor ?? null;
    if (!Array.isArray(data?.items) || data.items.length > pageSize
        || (next !== null && (typeof next !== "string" || !next || next.length > 2048 || next === cursor))) {
      throw new Error("Invalid website list response");
    }
    const items = data.items.map((site) => {
      const url = httpsURL(site?.url);
      if (!url || !url.hostname.endsWith(".pythonide.xin") || url.search || url.hash) {
        throw new Error("Invalid website URL");
      }
      return { site, url };
    });
    return { items, next };
  }

  function showState(state) {
    const loading = state === "loading" || state === "loading-more";
    const failed = state === "error" || state === "page-error";
    for (const line of statusLines) line.hidden = line.dataset.state !== state;
    list.setAttribute("aria-busy", String(loading));
    more.hidden = !nextCursor || failed;
    more.disabled = loading;
    retry.hidden = !failed;
  }

  async function load(cursor = null, trigger) {
    request?.abort();
    const controller = new AbortController();
    request = controller;
    const timeout = setTimeout(() => controller.abort(), requestTimeoutMS);
    showState(cursor ? "loading-more" : "loading");
    const url = new URL(feedURL);
    url.searchParams.set("limit", String(pageSize));
    if (query) url.searchParams.set("q", query);
    if (cursor) url.searchParams.set("cursor", cursor);

    try {
      const response = await fetch(url, {
        signal: controller.signal,
        credentials: "omit",
        referrerPolicy: "no-referrer",
        headers: { Accept: "application/json" },
      });
      if (!response.ok) throw new Error("Website list request failed");
      const { items, next } = readPage(await response.json(), cursor);
      if (request !== controller) return;

      const cards = [];
      for (const { site, url: siteURL } of items) {
        if (displayed.has(siteURL.href)) continue;
        cards.push(siteCard(site, siteURL));
        displayed.add(siteURL.href);
      }
      list.append(...cards);
      nextCursor = next;
      showState(list.childElementCount || nextCursor ? "ready" : query ? "no-results" : "empty");
      if (trigger && (document.activeElement === trigger || document.activeElement === document.body)) {
        cards[0]?.querySelector("[data-site-link]").focus();
      }
    } catch {
      if (request === controller) {
        showState(cursor ? "page-error" : "error");
        if (trigger && document.activeElement === document.body) retry.focus();
      }
    } finally {
      clearTimeout(timeout);
      if (request === controller) request = undefined;
    }
  }

  function reset(nextQuery) {
    query = nextQuery;
    search.value = query;
    latest.hidden = Boolean(query);
    results.hidden = !query;
    displayed.clear();
    list.replaceChildren();
    nextCursor = null;
    void load();
  }

  function queryFromURL() {
    return normalizedText(new URL(location.href).searchParams.get("q"), 80);
  }

  function setQuery(value) {
    const next = normalizedText(value, 80);
    if (next === query) return;
    const url = new URL(location.href);
    if (next) url.searchParams.set("q", next);
    else url.searchParams.delete("q");
    history.pushState(null, "", url.href);
    reset(next);
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    setQuery(search.value);
  });
  search.addEventListener("input", () => {
    if (!search.value) setQuery("");
  });
  more.addEventListener("click", () => {
    if (nextCursor && !request) void load(nextCursor, more);
  });
  retry.addEventListener("click", () => {
    if (!request) void load(nextCursor, retry);
  });
  addEventListener("popstate", () => {
    const previous = queryFromURL();
    if (previous !== query) reset(previous);
  });
  function updateSearchCopy() {
    search.placeholder = document.documentElement.lang === "en" ? "Name or domain" : "名称或域名";
    list.querySelectorAll(".showcase-cover-placeholder span").forEach(coverLabel);
  }
  document.addEventListener("pythonide:language", updateSearchCopy);

  form.hidden = false;
  updateSearchCopy();
  reset(queryFromURL());
}());
