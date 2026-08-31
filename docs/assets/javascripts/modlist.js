(() => {
  const GROUPS = [
    ["Tensura systems", /tensura|slimethrone|great sage|ascension|skill study|nightmare utils/i],
    ["Technology & crafting", /create|mekanism|silent gear|metalworks|iron furnaces|sophisticated|tom's simple|almostunified|polymorph|construction wand|spud's shops|chipped|rechiseled|reintegrated|crafting tweaks|easy anvils/i],
    ["Kingdoms & quests", /minecol|coloni|quest|ftb|byzantine|domum ornamentum|structurize|blockui/i],
    ["Adventure & world", /boss|artifact|apothic|cataclysm|mowzie|ice and fire|twilight|aether|deeper and darker|starlight|end remaster|dungeon|structure|biome|terralith|tectonic|loot|compass|waystone|legendary|farmer's delight|farmersstructures|sparse|torchmaster/i],
    ["Interface & client", /jade|just enough|apple ?skin|tooltip|betterf3|distant horizons|dynamic fps|iris|sodium|sound|music|mouse tweaks|inventory|configured|controlling|forgematica|entity model|entity texture|culling|pick up|item peek|trashslot|xaero|enchantment|fast item|euphoria|extreme sound|searchables/i],
    ["Multiplayer & server", /voice chat|chatmanager|connectivity|servercore|spark|chunky|luckperms|backup|grieflogger/i],
  ];

  const SUPPORT = /\b(api|lib|library|core|kubejs|kotlin|architectury|gecko|athena|balm|bookshelf|cloth config|collective|cupboard|curios|ephero|jupiter|konkrete|lithostitched|mafglib|moonlight|octolib|openloader|paxi|pigpen|placebo|player animator|prickle|puzzles|resourceful|rhino|runelic|silent lib|smartbrain|supermartijn|terrablender|uranus|oωo)\b|compat|addon example|tsr client stability/i;
  const ALLOWED_HOSTS = new Set(["www.curseforge.com", "curseforge.com", "modrinth.com", "www.modrinth.com", "github.com", "www.github.com", "serilum.com", "www.serilum.com"]);
  const normalize = (value) => String(value || "").toLocaleLowerCase().trim();

  function classify(mod) {
    const value = `${mod.name} ${mod.filename}`;
    if (SUPPORT.test(value)) return "Libraries & support";
    return GROUPS.find(([, pattern]) => pattern.test(value))?.[0] || "Other gameplay";
  }

  function safeProjectUrl(value) {
    try {
      const url = new URL(value);
      return url.protocol === "https:" && ALLOWED_HOSTS.has(url.hostname) ? url.href : null;
    } catch (_) {
      return null;
    }
  }

  function modCard(mod) {
    const card = document.createElement("article");
    const group = classify(mod);
    card.className = "current-mod-card";
    card.dataset.group = group;
    card.dataset.search = normalize(`${mod.name} ${mod.version} ${mod.filename} ${group}`);

    const heading = document.createElement("h2");
    heading.textContent = mod.name;
    const version = document.createElement("span");
    version.className = "current-mod-version";
    version.textContent = mod.version || "Version not declared";
    const badge = document.createElement("span");
    badge.className = "current-mod-group";
    badge.textContent = group;

    const metadata = document.createElement("div");
    metadata.className = "current-mod-meta";
    metadata.append(version, badge);

    const actions = document.createElement("div");
    actions.className = "current-mod-actions";
    const projectUrl = safeProjectUrl(mod.source_url);
    if (projectUrl) {
      const link = document.createElement("a");
      link.href = projectUrl;
      link.target = "_blank";
      link.rel = "noopener";
      link.textContent = "Project page ↗";
      actions.appendChild(link);
    } else {
      const local = document.createElement("span");
      local.textContent = "Pack-local module";
      actions.appendChild(local);
    }

    const details = document.createElement("details");
    const summary = document.createElement("summary");
    summary.textContent = "Technical details";
    const filename = document.createElement("code");
    filename.textContent = mod.filename;
    details.append(summary, filename);
    card.append(heading, metadata, actions, details);
    return card;
  }

  async function setup(root) {
    if (root.dataset.modlistReady === "true") return;
    root.dataset.modlistReady = "true";
    const grid = root.querySelector(".current-modlist-grid");
    const filters = root.querySelector(".current-modlist-filters");
    const input = root.querySelector(".current-modlist-search");
    const status = root.querySelector(".current-modlist-status");
    const empty = root.querySelector(".current-modlist-empty");

    try {
      const source = new URL(root.dataset.modlistSource, `${window.location.origin}/`);
      const response = await fetch(source, { credentials: "same-origin" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const snapshot = await response.json();
      const cards = snapshot.mods.map(modCard);
      grid.replaceChildren(...cards);
      const groups = ["All", ...new Set(cards.map((card) => card.dataset.group))];
      let activeGroup = "All";

      const apply = () => {
        const query = normalize(input.value);
        let visible = 0;
        cards.forEach((card) => {
          const show = (activeGroup === "All" || card.dataset.group === activeGroup) && (!query || card.dataset.search.includes(query));
          card.hidden = !show;
          if (show) visible += 1;
        });
        status.textContent = `Showing ${visible} of ${cards.length} mods`;
        empty.hidden = visible !== 0;
      };

      groups.forEach((group, index) => {
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = group;
        button.classList.toggle("is-active", index === 0);
        button.setAttribute("aria-pressed", String(index === 0));
        button.addEventListener("click", () => {
          activeGroup = group;
          filters.querySelectorAll("button").forEach((candidate) => {
            const active = candidate === button;
            candidate.classList.toggle("is-active", active);
            candidate.setAttribute("aria-pressed", String(active));
          });
          apply();
        });
        filters.appendChild(button);
      });
      input.addEventListener("input", apply);
      apply();
    } catch (_) {
      status.textContent = "The current modlist could not be loaded. Use the JSON snapshot link below.";
      root.classList.add("has-error");
    }
  }

  function boot() {
    document.querySelectorAll(".current-modlist").forEach(setup);
  }

  if (typeof document$ !== "undefined") document$.subscribe(boot);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
