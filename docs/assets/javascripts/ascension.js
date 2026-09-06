(() => {
  function revealTarget() {
    if (!location.hash) return;
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (_) { return; }
    const target = document.getElementById(id);
    if (target?.tagName === "DETAILS") target.open = true;
  }

  function boot() {
    revealTarget();
    document.querySelectorAll(".ascension-entry").forEach((entry) => {
      entry.addEventListener("toggle", () => {
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
