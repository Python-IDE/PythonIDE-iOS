/* Compatibility entry for older cached invitation pages. */
(function () {
  if (document.querySelector('script[src="/assets/site.js"]')) return;
  var script = document.createElement("script");
  script.src = "/assets/site.js";
  script.defer = true;
  document.head.appendChild(script);
}());
