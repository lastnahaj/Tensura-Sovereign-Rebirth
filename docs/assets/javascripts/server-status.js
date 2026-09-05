(() => {
  const API_ROOT = "https://api.mcsrvstat.us/3/";

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
    document.querySelectorAll("[data-server-status]").forEach(setupPanel);
  }

  if (typeof document$ !== "undefined") document$.subscribe(boot);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
