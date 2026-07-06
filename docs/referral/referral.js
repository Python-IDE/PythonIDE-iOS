const APP_STORE_URL = "https://apps.apple.com/app/id6753987304";
const APP_REFERRAL_URL = "pythonide://referral";

const copy = {
  zh: {
    brandSub: "邀请活动",
    navInvite: "邀请",
    navRules: "规则",
    navContact: "联系",
    download: "下载 App",
    copyCode: "复制邀请码",
    copied: "已复制",
    failed: "复制失败，请手动复制",
    invitedTitle: "好友邀请你使用 PythonIDE",
    invitedSummary: "下载 App 后输入邀请码，即可建立邀请关系。",
    inviteEntryTitle: "PythonIDE 邀请",
    inviteEntrySummary: "打开 App 后进入「我的」-「邀请好友」，即可查看并分享你的专属邀请码。",
    getInviteCode: "获取邀请码",
    noCodeToCopy: "当前页面没有邀请码",
    howWorks: "如何生效",
    viewRules: "查看活动规则",
    ruleTitle: "邀请活动规则",
    rewardTitle: "奖励档位",
    validTitle: "什么是有效邀请",
    otherTitle: "其他活动",
    footer: "活动解释权与兑换记录以后台数据为准",
    note: "奖励达到后请按 App 内邀请明细与后台记录联系兑换。Pro 月卡兑换以 App Store 弹窗为准，可在 App Store 账户设置取消订阅。截图不能作为有效邀请依据。",
    invalidCode: "邀请码",
    rewards: [
      ["10 位有效邀请", "Pro 月卡"],
      ["20 位有效邀请", "Pro 终身 5 折"],
      ["40 位有效邀请", "Pro 终身"],
    ],
    steps: [
      ["输入邀请码", "在 App 内「我的」-「输入邀请码」"],
      ["运行一次 Python 或使用 AI", "完成任意一次核心功能使用"],
      ["次日再次打开 App", "次日打开 App 即计为有效邀请"],
    ],
    valid: [
      ["首次使用的新用户", "老用户、重复设备和自邀不会计入"],
      ["绑定邀请码", "被邀请人只能绑定一次邀请码"],
      ["完成核心行为", "运行 Python 或使用 AI 功能"],
      ["次日仍打开 App", "完成留存验证后才计入有效邀请"],
    ],
    other: [
      ["小红书作品", "@我并获得 100 赞，可申请 Pro 终身兑换"],
      ["社区抽奖名额", "5000 人以上社区可申请 10 个 Pro 终身抽奖名额"],
    ],
    contactTitle: "领取 Pro 终身 5 折",
    contactSummary: "达到 20 位有效邀请后，请在 App 内提交申请，并带上申请编号联系开发者。",
    contactMethodTitle: "联系方式",
    contactMethodBody: "选择一个平台联系开发者，并发送申请编号。此页面会保持最新联系方式。",
    contactQQPending: "QQ（待补链接）",
    contactTelegram: "Telegram",
    contactXiaohongshu: "小红书",
    contactRequestTitle: "发送时包含",
    contactRequest1Title: "申请编号",
    contactRequest1Body: "在 App 的邀请页点击「Pro 终身 5 折」-「查看」，复制 REF 开头的编号。",
    contactRequest2Title: "你的邀请码",
    contactRequest2Body: "在 App 邀请页复制自己的邀请码，方便后台核对。",
    contactRequest3Title: "领取说明",
    contactRequest3Body: "说明你要领取 Pro 终身 5 折资格，不需要发送截图作为凭证。",
    contactNote: "最终是否满足条件，以后台有效邀请与领取记录为准。",
  },
  en: {
    brandSub: "Referral Program",
    navInvite: "Invite",
    navRules: "Rules",
    navContact: "Contact",
    download: "Download App",
    copyCode: "Copy Code",
    copied: "Copied",
    failed: "Copy failed. Please copy manually.",
    invitedTitle: "A friend invited you to PythonIDE",
    invitedSummary: "Download the app and enter this invite code to bind the referral.",
    inviteEntryTitle: "PythonIDE Referral",
    inviteEntrySummary: "Open the app, then go to Me - Invite Friends to find and share your personal invite code.",
    getInviteCode: "Get Invite Code",
    noCodeToCopy: "No invite code on this page.",
    howWorks: "How it counts",
    viewRules: "View rules",
    ruleTitle: "Referral Program Rules",
    rewardTitle: "Rewards",
    validTitle: "What counts as a valid referral",
    otherTitle: "Other campaigns",
    footer: "Final eligibility and redemption are based on backend records.",
    note: "After reaching a tier, use your in-app referral details to claim. For Pro Monthly, follow the App Store redemption prompt; subscriptions can be canceled in App Store account settings. Screenshots alone do not count as valid referrals.",
    invalidCode: "Invite Code",
    rewards: [
      ["10 valid referrals", "Pro Monthly"],
      ["20 valid referrals", "50% off Pro Lifetime"],
      ["40 valid referrals", "Pro Lifetime"],
    ],
    steps: [
      ["Enter the invite code", "In the app, open Me - Enter Invite Code"],
      ["Run Python once or use AI", "Complete one core action in the app"],
      ["Open the app the next day", "A return open confirms the referral"],
    ],
    valid: [
      ["A first-time new user", "Existing users, duplicate devices, and self-invites are excluded"],
      ["Invite code is bound", "Each invited user can bind only one code"],
      ["Core action completed", "Run Python or use AI"],
      ["Returns the next day", "Retention must be verified before it becomes valid"],
    ],
    other: [
      ["Xiaohongshu post", "@ me and reach 100 likes to apply for Pro Lifetime"],
      ["Community raffle", "Communities over 5,000 members may apply for 10 Pro Lifetime raffle slots"],
    ],
    contactTitle: "Claim 50% Off Pro Lifetime",
    contactSummary: "After reaching 20 valid referrals, submit the request in the app and contact the developer with your claim ID.",
    contactMethodTitle: "Contact",
    contactMethodBody: "Choose a platform below and send your claim ID. This page will keep the latest contact details.",
    contactQQPending: "QQ (link pending)",
    contactTelegram: "Telegram",
    contactXiaohongshu: "Xiaohongshu",
    contactRequestTitle: "Include these details",
    contactRequest1Title: "Claim ID",
    contactRequest1Body: "In the app referral page, tap Pro Lifetime 50% Off - View, then copy the ID starting with REF.",
    contactRequest2Title: "Your invite code",
    contactRequest2Body: "Copy your own invite code from the app referral page so the backend record can be checked.",
    contactRequest3Title: "Claim note",
    contactRequest3Body: "Say that you are claiming the 50% off Pro Lifetime reward. Screenshots are not required as proof.",
    contactNote: "Final eligibility is based on backend referral and claim records.",
  },
};

const iconPaths = {
  user: "M20 21a8 8 0 0 0-16 0M12 13a5 5 0 1 0 0-10 5 5 0 0 0 0 10Z",
  link: "M10 13a5 5 0 0 0 7.07 0l2-2a5 5 0 0 0-7.07-7.07l-1.2 1.2M14 11a5 5 0 0 0-7.07 0l-2 2A5 5 0 0 0 12 20.07l1.2-1.2",
  spark: "M12 2v5M12 17v5M4.22 4.22l3.54 3.54M16.24 16.24l3.54 3.54M2 12h5M17 12h5M4.22 19.78l3.54-3.54M16.24 7.76l3.54-3.54",
  clock: "M12 8v5l3 2M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z",
  gift: "M20 12v8a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-8M2 8h20v4H2V8ZM12 8v13M12 8H8.5A2.5 2.5 0 1 1 11 5.5L12 8Zm0 0h3.5A2.5 2.5 0 1 0 13 5.5L12 8Z",
  percent: "M19 5 5 19M7.5 8.5a2 2 0 1 0 0-4 2 2 0 0 0 0 4ZM16.5 19.5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z",
  crown: "M3 8l4.5 4L12 5l4.5 7L21 8l-2 11H5L3 8Z",
  pen: "M17 3l4 4L8 20H4v-4L17 3Z",
  community: "M16 20a4 4 0 0 0-8 0M12 13a4 4 0 1 0 0-8 4 4 0 0 0 0 8ZM22 20a3.5 3.5 0 0 0-5.4-2.95M17 11a3 3 0 1 0 0-6M2 20a3.5 3.5 0 0 1 5.4-2.95M7 11a3 3 0 1 1 0-6",
};

function routePath() {
  const fallback = new URLSearchParams(location.search).get("path");
  return fallback || `${location.pathname}${location.search}`;
}

function inviteCodeFromPath() {
  const raw = routePath();
  let url;
  try {
    url = new URL(raw, location.origin);
  } catch {
    return "";
  }
  const parts = url.pathname.split("/").filter(Boolean);
  const code = parts[0] === "i" && parts[1] ? parts[1] : url.searchParams.get("code");
  return normalizeCode(code);
}

function normalizeCode(value) {
  const cleaned = String(value || "").replace(/[\s-]+/g, "").toUpperCase();
  return /^[A-Z0-9]{4,12}$/.test(cleaned) ? cleaned : "";
}

function initialLanguage() {
  const fromQuery = new URLSearchParams(location.search).get("lang");
  if (fromQuery === "en" || fromQuery === "zh") return fromQuery;
  const saved = localStorage.getItem("referral_lang");
  if (saved === "en" || saved === "zh") return saved;
  return navigator.language && navigator.language.toLowerCase().startsWith("en") ? "en" : "zh";
}

function currentLanguage() {
  return document.documentElement.dataset.lang === "en" ? "en" : "zh";
}

function setLanguage(lang) {
  const active = lang === "en" ? "en" : "zh";
  localStorage.setItem("referral_lang", active);
  document.documentElement.lang = active === "en" ? "en" : "zh-CN";
  document.documentElement.dataset.lang = active;
  const t = copy[active];
  document.querySelectorAll("[data-t]").forEach((node) => {
    const key = node.dataset.t;
    if (t[key]) node.textContent = t[key];
  });
  document.querySelectorAll("[data-array]").forEach((node) => {
    renderArray(node, t);
  });
  document.querySelectorAll("[data-lang]").forEach((button) => {
    button.setAttribute("aria-pressed", button.dataset.lang === active ? "true" : "false");
  });
  document.querySelectorAll("[data-copy-feedback]").forEach((node) => {
    node.dataset.copyFeedback = t.copied;
  });
  applyInvitePageState(inviteCodeFromPath(), t);
  setupReveal();
  setupPointerMotion();
}

function renderArray(node, t) {
  const key = node.dataset.array;
  const rows = t[key] || [];
  if (key === "rewards") {
    const icons = ["gift", "percent", "crown"];
    node.innerHTML = rows.map(([requirement, reward], index) => `
      <div class="rule-row reveal">
        <div class="rule-icon" aria-hidden="true">${svgIcon(icons[index] || "gift")}</div>
        <div>
          <strong>${reward}</strong>
          <span>${requirement}</span>
        </div>
      </div>
    `).join("");
    return;
  }
  if (key === "steps") {
    node.innerHTML = rows.map(([title, detail], index) => `
      <div class="step reveal" style="--delay:${index * 90}ms">
        <div class="step-num">${index + 1}</div>
        <div>
          <strong>${index + 1}. ${title}</strong>
          <span>${detail}</span>
        </div>
      </div>
    `).join("");
    return;
  }
  if (key === "valid") {
    const icons = ["user", "link", "spark", "clock"];
    node.innerHTML = rows.map(([title, detail], index) => `
      <div class="rule-row reveal">
        <div class="rule-icon" aria-hidden="true">${svgIcon(icons[index] || "spark")}</div>
        <div>
          <strong>${title}</strong>
          <span>${detail}</span>
        </div>
      </div>
    `).join("");
    return;
  }
  if (key === "other") {
    const icons = ["pen", "community"];
    node.innerHTML = rows.map(([title, detail], index) => `
      <div class="rule-row reveal">
        <div class="rule-icon" aria-hidden="true">${svgIcon(icons[index] || "spark")}</div>
        <div>
          <strong>${title}</strong>
          <span>${detail}</span>
        </div>
      </div>
    `).join("");
  }
}

function svgIcon(name) {
  return `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="${iconPaths[name]}"></path></svg>`;
}

function renderInviteCode(code) {
  const target = document.querySelector("[data-invite-code]");
  if (!target) return;
  if (!code) {
    renderInvitePlaceholder(copy[currentLanguage()].getInviteCode);
    return;
  }
  target.dataset.inviteCode = code;
  target.dataset.length = String(code.length);
  target.classList.remove("invite-placeholder");
  target.classList.toggle("compact", code.length >= 7);
  target.classList.toggle("ultra-compact", code.length >= 10);
  target.removeAttribute("role");
  target.removeAttribute("tabindex");
  target.setAttribute("aria-label", `${copy[currentLanguage()].invalidCode} ${code}`);
  target.innerHTML = code.split("").map((char, index) => `<span style="--i:${index}">${char}</span>`).join("");
}

function renderInvitePlaceholder(label) {
  const target = document.querySelector("[data-invite-code]");
  if (!target) return;
  target.dataset.inviteCode = "";
  target.dataset.length = "0";
  target.classList.remove("compact", "ultra-compact");
  target.classList.add("invite-placeholder");
  target.setAttribute("role", "button");
  target.setAttribute("tabindex", "0");
  target.setAttribute("aria-label", label);
  target.textContent = label;
}

function applyInvitePageState(code, t) {
  const target = document.querySelector("[data-invite-code]");
  if (!target) {
    document.body.classList.remove("invite-missing-code");
    return;
  }

  const hasCode = Boolean(code);
  document.body.classList.toggle("invite-missing-code", !hasCode);

  const title = document.getElementById("invite-title");
  if (title) title.textContent = hasCode ? t.invitedTitle : t.inviteEntryTitle;

  const summary = document.querySelector("[data-invite-summary]");
  if (summary) summary.textContent = hasCode ? t.invitedSummary : t.inviteEntrySummary;

  const copyButton = document.querySelector("[data-copy-code]");
  if (copyButton) copyButton.hidden = !hasCode;

  const rulesButton = document.querySelector("[data-no-code-rules]");
  if (rulesButton) rulesButton.hidden = hasCode;

  if (hasCode) {
    renderInviteCode(code);
  } else {
    renderInvitePlaceholder(t.getInviteCode);
  }
}

async function copyInviteCode() {
  const code = document.querySelector("[data-invite-code]")?.dataset.inviteCode || inviteCodeFromPath();
  if (!code) {
    showToast(copy[currentLanguage()].noCodeToCopy);
    return;
  }
  try {
    await copyText(code);
    document.body.classList.add("code-copied");
    showToast(copy[document.documentElement.dataset.lang || "zh"].copied);
    const button = document.querySelector("[data-copy-code]");
    if (button) {
      button.classList.add("copied");
      window.setTimeout(() => button.classList.remove("copied"), 900);
    }
    window.setTimeout(() => document.body.classList.remove("code-copied"), 620);
  } catch {
    showToast(copy[document.documentElement.dataset.lang || "zh"].failed);
  }
}

function openReferralInApp() {
  const startedAt = Date.now();
  let didHide = false;
  const fallbackDelay = 900;
  const onVisibilityChange = () => {
    if (document.hidden) didHide = true;
  };

  document.addEventListener("visibilitychange", onVisibilityChange, { once: true });
  window.setTimeout(() => {
    document.removeEventListener("visibilitychange", onVisibilityChange);
    if (!didHide && Date.now() - startedAt < 1800) {
      window.location.href = APP_STORE_URL;
    }
  }, fallbackDelay);

  window.location.href = APP_REFERRAL_URL;
}

function activateInvitePlaceholder() {
  if (!document.body.classList.contains("invite-missing-code")) return;
  openReferralInApp();
}

async function copyText(text) {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(text);
    return;
  }
  const textarea = document.createElement("textarea");
  textarea.value = text;
  textarea.setAttribute("readonly", "");
  textarea.style.position = "fixed";
  textarea.style.left = "-9999px";
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  textarea.remove();
}

function showToast(message) {
  let toast = document.querySelector(".toast");
  if (!toast) {
    toast = document.createElement("div");
    toast.className = "toast";
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.classList.add("show");
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => toast.classList.remove("show"), 1600);
}

let revealObserver;

function setupReveal() {
  if (revealObserver) revealObserver.disconnect();
  if (!("IntersectionObserver" in window)) {
    document.querySelectorAll(".reveal").forEach((node) => node.classList.add("in"));
    return;
  }
  revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll(".reveal").forEach((node, index) => {
    node.style.setProperty("--reveal-delay", `${Math.min(index * 36, 220)}ms`);
    revealObserver.observe(node);
  });
}

function setupPointerMotion() {
  if (!setupPointerMotion.windowReady) {
    setupPointerMotion.windowReady = true;
    window.addEventListener("pointermove", (event) => {
      document.documentElement.style.setProperty("--pointer-x", `${event.clientX}px`);
      document.documentElement.style.setProperty("--pointer-y", `${event.clientY}px`);
    }, { passive: true });
  }

  document.querySelectorAll(".motion-surface").forEach((node) => {
    if (node.dataset.motionReady === "true") return;
    node.dataset.motionReady = "true";
    node.addEventListener("pointermove", (event) => {
      const rect = node.getBoundingClientRect();
      const x = (event.clientX - rect.left) / rect.width - 0.5;
      const y = (event.clientY - rect.top) / rect.height - 0.5;
      node.style.transform = `perspective(900px) rotateX(${(-y * 2).toFixed(2)}deg) rotateY(${(x * 2).toFixed(2)}deg) translateY(-1px)`;
    });
    node.addEventListener("pointerleave", () => {
      node.style.transform = "";
    });
  });

  document.querySelectorAll(".button").forEach((button) => {
    button.addEventListener("pointermove", (event) => {
      const rect = button.getBoundingClientRect();
      button.style.setProperty("--ripple-x", `${event.clientX - rect.left}px`);
      button.style.setProperty("--ripple-y", `${event.clientY - rect.top}px`);
    });
  });
}

function init() {
  document.querySelectorAll("[data-download]").forEach((node) => {
    node.setAttribute("href", APP_STORE_URL);
  });
  const inviteCode = document.querySelector("[data-invite-code]");
  if (inviteCode) {
    inviteCode.addEventListener("click", activateInvitePlaceholder);
    inviteCode.addEventListener("keydown", (event) => {
      if (event.key !== "Enter" && event.key !== " ") return;
      if (!document.body.classList.contains("invite-missing-code")) return;
      event.preventDefault();
      openReferralInApp();
    });
  }
  document.querySelectorAll("[data-copy-code]").forEach((node) => {
    node.addEventListener("click", copyInviteCode);
  });
  document.querySelectorAll("[data-lang]").forEach((node) => {
    node.addEventListener("click", () => setLanguage(node.dataset.lang));
  });
  setLanguage(initialLanguage());
}

document.addEventListener("DOMContentLoaded", init);
