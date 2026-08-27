(() => {
  const normalize = (value) => value.toLocaleLowerCase().trim();

  function setupDirectory(directory) {
    if (directory.dataset.referenceReady === "true") return;
    directory.dataset.referenceReady = "true";

    const input = directory.querySelector(".reference-filter-input");
    const buttons = Array.from(directory.querySelectorAll("[data-letter]"));
    const cards = Array.from(directory.querySelectorAll(".reference-card"));
    const status = directory.querySelector(".reference-filter-status");
    const empty = directory.querySelector(".reference-no-results");
    let activeLetter = "all";

    const applyFilter = () => {
      const query = normalize(input?.value || "");
      let visible = 0;
      cards.forEach((card) => {
        const matchesLetter = activeLetter === "all" || card.dataset.letter === activeLetter;
        const matchesQuery = !query || normalize(card.dataset.search || "").includes(query);
        const show = matchesLetter && matchesQuery;
        card.hidden = !show;
        if (show) visible += 1;
      });
      if (status) status.textContent = `Showing ${visible} of ${cards.length} articles`;
      if (empty) empty.hidden = visible !== 0;
    };

    input?.addEventListener("input", applyFilter);
    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        activeLetter = button.dataset.letter || "all";
        buttons.forEach((candidate) => {
          const active = candidate === button;
          candidate.classList.toggle("is-active", active);
          candidate.setAttribute("aria-pressed", String(active));
        });
        applyFilter();
      });
    });
  }

  function convertSections(article) {
    const root = article.querySelector(":scope > .mw-parser-output") || article.firstElementChild;
    if (!root || root.dataset.referenceSectionsReady === "true") return [];
    root.dataset.referenceSectionsReady = "true";
    const headings = Array.from(root.children).filter((node) => node.tagName === "H2");
    const details = [];

    headings.forEach((heading, index) => {
      const section = document.createElement("details");
      section.className = "reference-section";
      section.open = index < 2;
      const summary = document.createElement("summary");
      while (heading.firstChild) summary.appendChild(heading.firstChild);
      section.appendChild(summary);
      root.insertBefore(section, heading);

      let node = heading.nextSibling;
      heading.remove();
      while (node && !(node.nodeType === Node.ELEMENT_NODE && node.tagName === "H2")) {
        const next = node.nextSibling;
        section.appendChild(node);
        node = next;
      }
      details.push(section);
    });
    return details;
  }

  function setupReadingMode(details) {
    const buttons = Array.from(document.querySelectorAll(".reference-mode-button"));
    if (!buttons.length) return;

    const activate = (mode) => {
      details.forEach((section, index) => {
        section.open = mode === "full" || index < 2;
      });
      buttons.forEach((button) => {
        const active = button.dataset.referenceMode === mode;
        button.classList.toggle("is-active", active);
        button.setAttribute("aria-pressed", String(active));
      });
    };

    buttons.forEach((button) => {
      button.addEventListener("click", () => activate(button.dataset.referenceMode || "overview"));
    });
  }

  function revealHashTarget() {
    if (!window.location.hash) return;
    let id = window.location.hash.slice(1);
    try {
      id = decodeURIComponent(id);
    } catch (_) {
      return;
    }
    const target = document.getElementById(id);
    const section = target?.closest(".reference-section");
    if (section) section.open = true;
  }

  function setupLightbox(container) {
    let dialog = document.querySelector(".reference-lightbox");
    if (!dialog) {
      dialog = document.createElement("dialog");
      dialog.className = "reference-lightbox";
      dialog.innerHTML = '<button type="button" aria-label="Close image">×</button><img alt="">';
      document.body.appendChild(dialog);
      dialog.querySelector("button")?.addEventListener("click", () => dialog.close());
      dialog.addEventListener("click", (event) => {
        if (event.target === dialog) dialog.close();
      });
    }
    const dialogImage = dialog.querySelector("img");
    container.querySelectorAll(".reference-overview img, .tensura-reference-article img").forEach((image) => {
      if (image.closest("a") || image.dataset.referenceZoom === "true") return;
      image.dataset.referenceZoom = "true";
      image.tabIndex = 0;
      image.setAttribute("role", "button");
      image.setAttribute("aria-label", image.alt ? `Enlarge ${image.alt}` : "Enlarge image");
      const open = () => {
        dialogImage.src = image.currentSrc || image.src;
        dialogImage.alt = image.alt || "Enlarged source image";
        dialog.showModal();
      };
      image.addEventListener("click", open);
      image.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          open();
        }
      });
    });
  }

  function setupProgress(article) {
    document.querySelector(".reference-progress")?.remove();
    const progress = document.createElement("div");
    progress.className = "reference-progress";
    progress.setAttribute("aria-hidden", "true");
    document.body.appendChild(progress);

    const update = () => {
      const rect = article.getBoundingClientRect();
      const total = Math.max(article.scrollHeight - window.innerHeight * 0.45, 1);
      const completed = Math.min(Math.max(-rect.top + window.innerHeight * 0.22, 0), total);
      progress.style.width = `${(completed / total) * 100}%`;
    };
    window.addEventListener("scroll", update, { passive: true });
    update();
  }

  function boot() {
    document.querySelectorAll(".reference-directory").forEach(setupDirectory);
    const article = document.querySelector(".tensura-reference-article");
    if (!article || article.dataset.referenceReady === "true") return;
    article.dataset.referenceReady = "true";
    const details = convertSections(article);
    setupReadingMode(details);
    setupLightbox(document);
    setupProgress(article);
    revealHashTarget();
    window.addEventListener("hashchange", revealHashTarget);
  }

  if (typeof document$ !== "undefined") {
    document$.subscribe(boot);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
