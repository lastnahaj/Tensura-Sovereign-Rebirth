/* Local ability lookup; gameplay and eligibility remain in the source catalogue. */
(() => {
  'use strict';
  const script = document.currentScript;
  if (!script) return;
  const root = new URL('../../', script.src);
  const indexURL = new URL('../data/skill-search.json', script.src);
  let indexPromise;
  const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
  const label = category => category.split('/').pop().replace(/^./, character => character.toUpperCase());
  function boot() {
    const hub = document.querySelector('.skill-hub');
    if (!hub || hub.dataset.searchReady) return;
    hub.dataset.searchReady = 'true';
    const input = hub.querySelector('#skill-hub-search');
    const clear = hub.querySelector('[data-clear-skill-search]');
    const status = hub.querySelector('.skill-finder-status');
    const results = hub.querySelector('.skill-finder-results');
    const initialStatus = status.textContent;
    let revision = 0;
    async function search() {
      const version = ++revision;
      const query = normalize(input.value);
      results.replaceChildren();
      results.hidden = true;
      if (!query) { status.textContent = initialStatus; return; }
      status.textContent = 'Searching the ability index…';
      try {
        if (!indexPromise) indexPromise = fetch(indexURL).then(response => {
          if (!response.ok) throw new Error('Index unavailable');
          return response.json();
        }).catch(error => { indexPromise = undefined; throw error; });
        const entries = await indexPromise;
        if (version !== revision) return;
        const words = query.split(/\s+/);
        const matches = entries.filter(entry => words.every(word => normalize(`${entry.title} ${label(entry.category)}`).includes(word)));
        matches.sort((a, b) => Number(normalize(b.title) === query) - Number(normalize(a.title) === query));
        const displayed = matches.slice(0, 18);
        status.textContent = matches.length
          ? `${matches.length} ${matches.length === 1 ? 'ability' : 'abilities'} found.${matches.length > displayed.length ? ' Showing the first 18; refine your search for more specific results.' : ''}`
          : 'No matching abilities. Try a shorter name, or browse a category below.';
        for (const entry of displayed) {
          const link = document.createElement('a');
          link.className = 'skill-search-result';
          link.href = new URL(entry.route, root).href;
          if (entry.image) {
            const image = document.createElement('img');
            image.src = new URL(entry.image, root).href;
            image.alt = '';
            image.loading = 'lazy';
            link.append(image);
          }
          const copy = document.createElement('span');
          const title = document.createElement('strong');
          title.textContent = entry.title;
          const type = document.createElement('small');
          type.textContent = label(entry.category);
          copy.append(title, type);
          if (entry.status === 'reference') {
            const pending = document.createElement('small');
            pending.className = 'skill-search-pending';
            pending.textContent = 'Server build match pending';
            copy.append(pending);
          }
          link.append(copy);
          results.append(link);
        }
        results.hidden = !displayed.length;
      } catch {
        if (version === revision) status.textContent = 'Search is unavailable. Use the category links below to browse abilities.';
      }
    }
    input.addEventListener('input', search);
    clear.addEventListener('click', () => { input.value = ''; search(); input.focus(); });
    if (input.value) search();
  }
  if (typeof document$ !== 'undefined') document$.subscribe(boot);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
