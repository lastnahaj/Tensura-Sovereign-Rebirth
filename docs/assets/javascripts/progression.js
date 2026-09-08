(() => {
  const scriptUrl = new URL(document.currentScript.src);
  const siteRoot = new URL("../../", scriptUrl);
  const dataUrl = new URL("../data/progression.json", scriptUrl);
  let graphRequest;

  function card(graph, key, edge) {
    const node = graph.nodes[key];
    const link = document.createElement("a");
    link.className = "reference-related-card";
    link.href = new URL(key, siteRoot).href;
    if (node.image) {
      const image = document.createElement("img");
      image.src = new URL(node.image, siteRoot).href;
      image.alt = "";
      image.loading = "lazy";
      link.append(image);
    }
    const copy = document.createElement("span");
    copy.className = "reference-related-copy";
    const title = document.createElement("strong");
    title.textContent = node.title;
    const description = document.createElement("small");
    const requirements = edge.requirements.filter((text) => text.trim().toLowerCase() !== node.title.trim().toLowerCase());
    description.textContent = requirements.join(" · ") || edge.kinds.join(" · ");
    copy.append(title);
    if (node.verification === "reference-build-only") {
      const status = document.createElement("small");
      status.className = "skill-reference-status";
      status.textContent = "Server build match pending";
      copy.append(status);
    }
    copy.append(description);
    link.append(copy);
    return link;
  }

  async function boot() {
    const article = document.querySelector(".tensura-reference-article, .maintained-skill-article");
    if (!article || document.querySelector(".reference-progression")) return;
    graphRequest ||= fetch(dataUrl).then((response) => {
      if (!response.ok) throw new Error("Progression reference unavailable");
      return response.json();
    });
    let graph;
    try { graph = await graphRequest; } catch (_) { graphRequest = null; return; }
    if (!article.isConnected) return;
    const key = decodeURIComponent(location.pathname.slice(siteRoot.pathname.length));
    const previous = graph.edges.filter((edge) => edge.to === key);
    const next = graph.edges.filter((edge) => edge.from === key);
    if (!previous.length && !next.length) return;
    const section = document.createElement("section");
    section.className = "reference-progression";
    section.setAttribute("aria-label", "Documented progression connections");
    for (const [title, edges, direction] of [["Previous stages & prerequisites", previous, "from"], ["Next stages & unlocks", next, "to"]]) {
      if (!edges.length) continue;
      const group = document.createElement("div");
      const heading = document.createElement("h2");
      heading.textContent = title;
      const grid = document.createElement("div");
      grid.className = "reference-related-grid";
      edges.forEach((edge) => grid.append(card(graph, edge[direction], edge)));
      group.append(heading, grid);
      section.append(group);
    }
    article.before(section);
    document.querySelector(".reference-related")?.remove();
  }

  if (typeof document$ !== "undefined") document$.subscribe(boot);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
