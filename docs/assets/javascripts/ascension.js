(() => {
  const scriptUrl = new URL(document.currentScript.src);

  async function redirectLegacySkill() {
    if (!document.querySelector("[data-skill-redirect]")) return;
    try {
      const response = await fetch(new URL("../data/skill-redirects.json", scriptUrl));
      if (!response.ok) return;
      const destinations = await response.json();
      const root = new URL("../../", scriptUrl);
      const path = location.pathname.slice(root.pathname.length);
      const destination = destinations[path + location.hash] || destinations[path];
      if (destination) location.replace(new URL(destination, root));
    } catch (_) { /* The page retains ordinary links when a redirect is unavailable. */ }
  }

  function revealTarget() {
    if (!location.hash) return;
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
    const target = document.getElementById(id);
    const entry = target?.closest("details.ascension-entry");
    if (entry) entry.open = true;
  }

  function boot() {
    redirectLegacySkill();
    revealTarget();
    document.querySelectorAll(".ascension-entry").forEach((entry) => {
      if (entry.dataset.ascensionReady === "true") return;
      entry.dataset.ascensionReady = "true";
      entry.addEventListener("toggle", () => {
        let target;
        try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (_) { return; }
        if (target && entry.contains(target)) return;
        if (entry.open && entry.id && location.hash !== `#${entry.id}`) {
          history.replaceState(null, "", `#${entry.id}`);
        }
      });
    });
  }

  window.addEventListener("hashchange", revealTarget);
  if (typeof document$ !== "undefined") document$.subscribe(boot);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
