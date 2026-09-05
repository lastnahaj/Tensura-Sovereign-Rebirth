(() => {
  const STORAGE_KEY = "tsr-onboarding-checklist-v1";

  function loadProgress() {
    try {
      return new Set(JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]"));
    } catch (_) {
      return new Set();
    }
  }

  function saveProgress(values) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(Array.from(values)));
    } catch (_) {
      // The checklist still works for this page view when storage is unavailable.
    }
  }

  function setupChecklist(root) {
    if (root.dataset.checklistReady === "true") return;
    root.dataset.checklistReady = "true";
    const inputs = Array.from(root.querySelectorAll("input[data-check-id]"));
    const progress = root.querySelector("progress");
    const label = root.querySelector("[data-checklist-count]");
    const completed = loadProgress();

    const render = () => {
      inputs.forEach((input) => {
        input.checked = completed.has(input.dataset.checkId);
      });
      const count = inputs.filter((input) => input.checked).length;
      if (progress) {
        progress.max = inputs.length;
        progress.value = count;
      }
      if (label) label.textContent = `${count} of ${inputs.length} field tasks complete`;
    };

    inputs.forEach((input) => {
      input.addEventListener("change", () => {
        if (input.checked) completed.add(input.dataset.checkId);
        else completed.delete(input.dataset.checkId);
        saveProgress(completed);
        render();
      });
    });
    root.querySelector("[data-checklist-reset]")?.addEventListener("click", () => {
      completed.clear();
      saveProgress(completed);
      render();
    });
    render();
  }

  function setupPaths(root) {
    if (root.dataset.pathsReady === "true") return;
    root.dataset.pathsReady = "true";
    const tabs = Array.from(root.querySelectorAll("[role='tab']"));
    const panels = Array.from(root.querySelectorAll("[role='tabpanel']"));

    const activate = (tab) => {
      tabs.forEach((candidate) => {
        const selected = candidate === tab;
        candidate.setAttribute("aria-selected", String(selected));
        candidate.tabIndex = selected ? 0 : -1;
      });
      panels.forEach((panel) => {
        panel.hidden = panel.id !== tab.getAttribute("aria-controls");
      });
    };

    tabs.forEach((tab, index) => {
      tab.addEventListener("click", () => activate(tab));
      tab.addEventListener("keydown", (event) => {
        if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
        event.preventDefault();
        let next = index;
        if (event.key === "ArrowLeft") next = (index - 1 + tabs.length) % tabs.length;
        if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
        if (event.key === "Home") next = 0;
        if (event.key === "End") next = tabs.length - 1;
        activate(tabs[next]);
        tabs[next].focus();
      });
    });
    if (tabs[0]) activate(tabs.find((tab) => tab.getAttribute("aria-selected") === "true") || tabs[0]);
  }

  function boot() {
    document.querySelectorAll("[data-onboarding-checklist]").forEach(setupChecklist);
    document.querySelectorAll("[data-onboarding-paths]").forEach(setupPaths);
  }

  if (typeof document$ !== "undefined") document$.subscribe(boot);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
