(() => {
  "use strict";

  const text = {
    en: { title: "Release Notes", language: "Language", version: "Version", all: "All versions",
      loading: "Loading release notes…", failed: "Couldn’t load release notes.", retry: "Try Again" },
    es: { title: "Notas de la versión", language: "Idioma", version: "Versión", all: "Todas las versiones",
      loading: "Cargando las notas…", failed: "No se pudieron cargar las notas.", retry: "Reintentar" },
    "pt-BR": { title: "Notas da versão", language: "Idioma", version: "Versão", all: "Todas as versões",
      loading: "Carregando as notas…", failed: "Não foi possível carregar as notas.", retry: "Tentar novamente" },
    de: { title: "Versionsverlauf", language: "Sprache", version: "Version", all: "Alle Versionen",
      loading: "Versionsverlauf wird geladen…", failed: "Der Versionsverlauf konnte nicht geladen werden.", retry: "Erneut versuchen" },
    fr: { title: "Notes de version", language: "Langue", version: "Version", all: "Toutes les versions",
      loading: "Chargement des notes de version…", failed: "Impossible de charger les notes de version.", retry: "Réessayer" },
    "zh-Hans": { title: "更新日志", language: "语言", version: "版本", all: "所有版本",
      loading: "正在加载更新日志…", failed: "加载更新日志失败。", retry: "重试" },
    "zh-Hant": { title: "版本記錄", language: "語言", version: "版本", all: "所有版本",
      loading: "正在載入版本記錄…", failed: "無法載入版本記錄。", retry: "重試" },
    ja: { title: "アップデート履歴", language: "言語", version: "バージョン", all: "すべてのバージョン",
      loading: "アップデート履歴を読み込んでいます…", failed: "アップデート履歴を読み込めませんでした。", retry: "再試行" },
    ko: { title: "업데이트 내역", language: "언어", version: "버전", all: "모든 버전",
      loading: "업데이트 내역을 불러오는 중…", failed: "업데이트 내역을 불러오지 못했습니다.", retry: "다시 시도" },
    ru: { title: "История версий", language: "Язык", version: "Версия", all: "Все версии",
      loading: "Загрузка истории версий…", failed: "Не удалось загрузить историю версий.", retry: "Повторить" },
  };
  const byID = id => document.getElementById(id);
  const languageSelect = byID("changelog-language");
  const versionSelect = byID("changelog-version");
  const releaseList = byID("changelog-releases");
  const status = byID("changelog-status");
  const retry = byID("changelog-retry");
  const localeIDs = Object.keys(text);
  const versionPattern = /^v\d+\.\d+\.\d+$/;
  const query = new URLSearchParams(location.search);
  let releases;
  let failed = false;
  let language = [query.get("lang"), ...navigator.languages].map(matchLocale).find(Boolean) ?? "en";

  function matchLocale(tag) {
    const parts = (tag ?? "").toLowerCase().replaceAll("_", "-").split("-");
    const exact = localeIDs.find(id => id.toLowerCase() === parts.join("-"));
    if (exact) return exact;
    if (parts[0] === "zh") {
      if (parts.includes("hant")) return "zh-Hant";
      if (parts.includes("hans")) return "zh-Hans";
      return ["tw", "hk", "mo"].some(region => parts.includes(region)) ? "zh-Hant" : "zh-Hans";
    }
    return parts[0] === "pt" ? "pt-BR" : localeIDs.find(id => id === parts[0]);
  }

  function versionTarget() {
    const anchor = location.hash.slice(1);
    return versionPattern.test(anchor) ? byID(anchor) : null;
  }

  function syncSelectedVersion(scroll = false) {
    const target = versionTarget();
    releaseList.querySelector('[aria-current="location"]')?.removeAttribute("aria-current");
    target?.setAttribute("aria-current", "location");
    versionSelect.value = target?.id ?? "";
    if (scroll && target) {
      if (target === releaseList.firstElementChild) window.scrollTo(0, 0);
      else target.scrollIntoView({ block: "start" });
    }
  }

  function releaseArticle(release) {
    const article = document.createElement("article");
    article.className = "changelog-release";
    article.id = "v" + release.version;
    const heading = document.createElement("h2");
    const permalink = document.createElement("a");
    const url = new URL(location.href);
    url.searchParams.set("lang", language);
    url.hash = article.id;
    permalink.href = url.search + url.hash;
    permalink.textContent = release.version;
    heading.append(permalink);

    const list = document.createElement("ol");
    for (const highlight of release.highlights) {
      const notes = highlight.localizations[language];
      const item = document.createElement("li");
      const title = document.createElement("strong");
      const detail = document.createElement("p");
      title.textContent = notes.title;
      detail.textContent = notes.detail;
      item.append(title, detail);
      list.append(item);
    }
    article.append(heading, list);
    return article;
  }

  function render() {
    const labels = text[language];
    document.documentElement.lang = language;
    document.title = labels.title + " — PythonIDE";
    byID("changelog-home").href = language.startsWith("zh") ? "/" : "/?lang=en";
    byID("changelog-title").textContent = labels.title;
    byID("changelog-language-label").textContent = labels.language;
    byID("changelog-version-label").textContent = labels.version;
    byID("changelog-all-versions").textContent = labels.all;
    languageSelect.value = language;
    status.textContent = releases ? "" : failed ? labels.failed : labels.loading;
    retry.textContent = labels.retry;
    retry.hidden = !failed;
    if (releases) {
      releaseList.replaceChildren(...releases.map(releaseArticle));
      syncSelectedVersion(true);
    }
  }

  async function load() {
    failed = false;
    render();
    try {
      const response = await fetch("/changelog/releases.json", { cache: "no-cache" });
      if (!response.ok) throw new Error("Release history is unavailable");
      const archive = await response.json();
      if (archive.schemaVersion !== 1 || !Array.isArray(archive.releases) || !archive.releases.length) {
        throw new Error("Invalid release history");
      }
      releases = archive.releases;
      render();
      for (const release of releases) {
        versionSelect.add(new Option(release.version, "v" + release.version));
      }
      byID("changelog-jump").hidden = false;
      syncSelectedVersion();
    } catch {
      releases = undefined;
      failed = true;
      render();
    }
  }

  languageSelect.addEventListener("change", () => {
    language = languageSelect.value;
    const url = new URL(location.href);
    url.searchParams.set("lang", language);
    history.replaceState(null, "", url);
    render();
  });

  versionSelect.addEventListener("change", () => {
    const version = versionSelect.value;
    if (version) {
      location.hash = version;
    } else {
      const url = new URL(location.href);
      url.hash = "";
      history.replaceState(null, "", url);
      syncSelectedVersion();
      window.scrollTo(0, 0);
    }
  });
  window.addEventListener("hashchange", () => syncSelectedVersion(true));
  retry.addEventListener("click", load);
  load();
})();
