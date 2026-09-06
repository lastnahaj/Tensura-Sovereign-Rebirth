(() => {
  const API_ROOT = "https://api.mcsrvstat.us/3/";

  function createRailPanel() {
    const existing = document.querySelector(".tsr-live-realm-item");
    if (existing) return existing.querySelector("[data-server-status]");

    const navList = document.querySelector(".md-sidebar--primary .md-nav--primary > .md-nav__list");
    if (!navList) return null;

    // Reference articles share their collection's navigation context.
    if (!navList.querySelector(".md-nav__item--active")) {
      const current = location.pathname;
      const match = [...navList.querySelectorAll("a.md-nav__link[href]")]
        .filter((link) => {
          const path = new URL(link.href).pathname;
          return path !== "/" && current.startsWith(path);
        })
        .sort((a, b) => new URL(b.href).pathname.length - new URL(a.href).pathname.length)[0];
      let parent = match?.closest(".md-nav__item");
      while (parent && navList.contains(parent)) {
        parent.classList.add("md-nav__item--active");
        const toggle = parent.querySelector(":scope > .md-nav__toggle");
        if (toggle) toggle.checked = true;
        parent = parent.parentElement?.closest(".md-nav__item");
      }
    }

    const item = document.createElement("li");
    item.className = "md-nav__item tsr-live-realm-item";
    item.innerHTML = `
      <section class="server-pulse server-pulse--rail" data-server-status data-server-address="tsr.infinitegamingservers.com" aria-labelledby="rail-realm-status-title">
        <div class="server-pulse-heading">
          <p class="reference-eyebrow">Live realm</p>
          <span class="server-state" data-status-label>Checking…</span>
        </div>
        <p class="server-address"><span>Join address</span><strong>tsr.infinitegamingservers.com</strong></p>
        <div class="server-stat-grid">
          <div><strong data-status-online>—</strong><span>Online</span></div>
          <div><strong data-status-max>—</strong><span>Capacity</span></div>
          <div><strong data-status-version>—</strong><span>Version</span></div>
        </div>
        <p class="server-message" id="rail-realm-status-title" data-status-message>Requesting the latest cached public server status.</p>
        <ul class="server-player-list" data-status-players aria-label="Publicly reported online players"><li class="server-player-empty">Checking the public player sample…</li></ul>
        <div class="server-pulse-actions">
          <button type="button" data-copy-server>Copy server address</button>
          <button type="button" data-status-refresh>Refresh status</button>
          <span data-status-updated aria-live="polite"></span>
        </div>
        <p class="server-fine-print">Public status may be cached for five minutes. Names appear only when the server shares them.</p>
      </section>`;

    const homeItem = navList.firstElementChild;
    homeItem?.classList.add("tsr-home-nav-item");
    if (homeItem) homeItem.insertAdjacentElement("afterend", item);
    else navList.appendChild(item);
    return item.querySelector("[data-server-status]");
  }

  const setText = (root, selector, value) => {
    const target = root.querySelector(selector);
    if (target) target.textContent = value;
  };

  function renderPlayers(root, players, emptyMessage) {
    const list = root.querySelector("[data-status-players]");
    if (!list) return;
    list.replaceChildren();

    const online = Number(players?.online || 0);
    const publicPlayers = Array.isArray(players?.list) ? players.list.slice(0, 24) : [];
    if (!online) {
      const item = document.createElement("li");
      item.className = "server-player-empty";
      item.textContent = emptyMessage || "No players are currently reported online.";
      list.appendChild(item);
      return;
    }
    if (!publicPlayers.length) {
      const item = document.createElement("li");
      item.className = "server-player-empty";
      item.textContent = `${online} online · player names are not shared by the server.`;
      list.appendChild(item);
      return;
    }

    publicPlayers.forEach((player) => {
      const item = document.createElement("li");
      item.textContent = typeof player === "string" ? player : player?.name || "Adventurer";
      list.appendChild(item);
    });
    if (online > publicPlayers.length) {
      const item = document.createElement("li");
      item.className = "server-player-more";
      item.textContent = `+${online - publicPlayers.length} more`;
      list.appendChild(item);
    }
  }

  function renderOffline(root) {
    root.dataset.serverState = "offline";
    setText(root, "[data-status-label]", "Offline");
    setText(root, "[data-status-online]", "0");
    setText(root, "[data-status-max]", "—");
    setText(root, "[data-status-version]", "—");
    setText(root, "[data-status-message]", "The realm may be stopped or restarting. You can still copy the address and try again shortly.");
    renderPlayers(root, { online: 0 });
  }

  function renderUnavailable(root) {
    root.dataset.serverState = "unavailable";
    setText(root, "[data-status-label]", "Status unavailable");
    setText(root, "[data-status-online]", "—");
    setText(root, "[data-status-max]", "—");
    setText(root, "[data-status-version]", "—");
    setText(root, "[data-status-message]", "The public status service did not answer. This does not necessarily mean the server is offline.");
    renderPlayers(root, null, "Player list unavailable while the status service is unavailable.");
  }

  function renderOnline(root, payload) {
    const players = payload.players || {};
    root.dataset.serverState = "online";
    setText(root, "[data-status-label]", "Online");
    setText(root, "[data-status-online]", String(players.online ?? 0));
    setText(root, "[data-status-max]", String(players.max ?? "—"));
    setText(root, "[data-status-version]", payload.version || "Minecraft 1.21.1");
    setText(root, "[data-status-message]", "The realm is answering public Minecraft status requests.");
    renderPlayers(root, players);
  }

  async function refresh(root) {
    const address = root.dataset.serverAddress;
    const refreshButton = root.querySelector("[data-status-refresh]");
    if (!address || root.dataset.serverLoading === "true") return;

    root.dataset.serverLoading = "true";
    root.dataset.serverState = "loading";
    root.setAttribute("aria-busy", "true");
    refreshButton?.setAttribute("disabled", "");
    setText(root, "[data-status-label]", "Checking…");
    setText(root, "[data-status-message]", "Requesting the latest cached public server status.");

    const controller = new AbortController();
    const timer = window.setTimeout(() => controller.abort(), 9000);
    try {
      const response = await fetch(`${API_ROOT}${encodeURIComponent(address)}`, {
        headers: { Accept: "application/json" },
        signal: controller.signal,
      });
      if (!response.ok) throw new Error(`Status service returned ${response.status}`);
      const payload = await response.json();
      if (payload.online) renderOnline(root, payload);
      else renderOffline(root);
    } catch (_) {
      renderUnavailable(root);
    } finally {
      window.clearTimeout(timer);
      delete root.dataset.serverLoading;
      root.removeAttribute("aria-busy");
      refreshButton?.removeAttribute("disabled");
      setText(
        root,
        "[data-status-updated]",
        `Checked ${new Intl.DateTimeFormat(undefined, { hour: "numeric", minute: "2-digit" }).format(new Date())}`,
      );
    }
  }

  function setupPanel(root) {
    if (root.dataset.serverReady === "true") return;
    root.dataset.serverReady = "true";
    root.querySelector("[data-status-refresh]")?.addEventListener("click", () => refresh(root));

    const copyButton = root.querySelector("[data-copy-server]");
    copyButton?.addEventListener("click", async () => {
      const address = root.dataset.serverAddress || "";
      try {
        await navigator.clipboard.writeText(address);
        copyButton.textContent = "Address copied";
      } catch (_) {
        copyButton.textContent = address;
      }
      window.setTimeout(() => {
        copyButton.textContent = "Copy server address";
      }, 2200);
    });
    refresh(root);
  }

  function boot() {
    createRailPanel();
    document.querySelectorAll("[data-server-status]").forEach(setupPanel);
  }

  if (typeof document$ !== "undefined") document$.subscribe(boot);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
