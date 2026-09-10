(() => {
  const soulGradeTiers = [
    { min: 61, rank: "Supreme", locks: 3, range: "Soul Grade 61+" },
    { min: 51, rank: "Grand", locks: 2, range: "Soul Grade 51–60" },
    { min: 41, rank: "Greater", locks: 2, range: "Soul Grade 41–50" },
    { min: 31, rank: "High", locks: 2, range: "Soul Grade 31–40" },
    { min: 21, rank: "Medium", locks: 1, range: "Soul Grade 21–30" },
    { min: 11, rank: "Low", locks: 1, range: "Soul Grade 11–20" },
    { min: 0, rank: "Unranked", locks: 0, range: "Soul Grade 0–10" },
  ];

  function setupSoulGrade(root) {
    if (root.dataset.progressionReady === "true") return;
    root.dataset.progressionReady = "true";
    const input = root.querySelector("[data-soul-grade-input]");
    const output = root.querySelector("[data-soul-grade-output]");
    const meter = root.querySelector("[data-soul-grade-meter]");
    if (!input || !output) return;

    const render = () => {
      const grade = Math.max(0, Math.floor(Number(input.value) || 0));
      const tier = soulGradeTiers.find((candidate) => grade >= candidate.min);
      input.value = String(grade);
      output.innerHTML = "";
      const result = document.createElement("strong");
      result.textContent = `${tier.locks} ${tier.locks === 1 ? "lock" : "locks"}`;
      const detail = document.createElement("span");
      detail.textContent = `${tier.rank} · ${tier.range}`;
      output.append(result, detail);
      if (meter) meter.style.width = `${Math.min(100, (grade / 61) * 100)}%`;
    };

    input.addEventListener("input", render);
    input.addEventListener("change", render);
    render();
  }

  function setupPrestigeDirectory(root) {
    if (root.dataset.progressionReady === "true") return;
    root.dataset.progressionReady = "true";
    const input = root.querySelector("[data-prestige-search]");
    const cards = Array.from(root.querySelectorAll("[data-prestige-card]"));
    const count = root.querySelector("[data-prestige-count]");
    const empty = root.querySelector("[data-prestige-empty]");
    if (!input || !cards.length) return;

    const render = () => {
      const query = input.value.trim().toLocaleLowerCase();
      let visible = 0;
      cards.forEach((card) => {
        const haystack = `${card.dataset.search || ""} ${card.textContent}`.toLocaleLowerCase();
        const matches = !query || haystack.includes(query);
        card.hidden = !matches;
        if (!matches) card.open = false;
        if (matches) visible += 1;
      });
      if (count) count.textContent = `${visible} ${visible === 1 ? "challenge" : "challenges"} shown`;
      if (empty) empty.hidden = visible !== 0;
    };

    input.addEventListener("input", render);
    render();
  }

  function boot() {
    document.querySelectorAll("[data-soul-grade-calculator]").forEach(setupSoulGrade);
    document.querySelectorAll("[data-prestige-directory]").forEach(setupPrestigeDirectory);
  }

  if (typeof document$ !== "undefined") document$.subscribe(boot);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
