# shanezshertz-site

The Shanez Shertz homepage, live at `shanezshertz.shop`. A static page — no framework, no JS bundler — but the HTML itself is generated from data. The homepage is a scrolling illustrated street: each open collection is a storefront you scroll past (wheel, trackpad, touch, or drag), and each one links straight to its shop.

## Structure

- `collections.json` — one entry per collection: `slug`, `name`, `status` (`"open"` or `"coming-soon"`), `description`, `redirect` (required only when `status` is `"open"`), and `featured_title` (the caption for its card in the "A Taste of Every Shop" grid, required only when `status` is `"open"`).
- `build.py` — reads `collections.json`, writes `docs/index.html`. Run `python build.py` after editing `collections.json`.
- `docs/` — served by GitHub Pages (custom domain via `docs/CNAME`).
- `docs/styles.css` — all styling (the storefront street and the featured grid already scale to any number of collections, no CSS changes needed to add more).
- `docs/assets/` — logo and hero banner.
- `docs/assets/storefronts/<slug>.png` — the illustrated storefront shown in the scrolling street. Transparent background, consistent eye-level perspective across shops.
- `docs/assets/products/<slug>.jpg` — one representative product shot per collection, used in the featured grid.
- `docs/404.html` — hand-written, not generated, but shares the same header/footer markup as the generated homepage.

**The one deliberate exception to "no JS":** a ~10-line inline script remaps vertical mouse-wheel input to horizontal scrolling on the storefront street (trackpad, touch, and scrollbar-drag already scroll it natively with zero JS — this is only for a plain mouse wheel). It's a no-dependency progressive enhancement, not a build step.

A collection with status `"open"` needs both asset files in place before running `build.py` — there's nothing to draw in the street or feature in the grid for a shop that hasn't been illustrated yet.

## Adding a collection

1. Append an entry to `collections.json` (status `"coming-soon"`, no `redirect` yet).
2. Run `python build.py`.
3. Commit and push.

## Launching a collection that's already "coming-soon"

1. Add `docs/assets/storefronts/<slug>.png` and `docs/assets/products/<slug>.jpg` (see "Structure" above for what each needs).
2. In `collections.json`, change its `status` to `"open"`, add its `redirect` (the `go.shanezshertz.shop/<slug>` collection-level redirect — set that up in `shanezshertz-go` first), and add `featured_title`.
3. Run `python build.py`.
4. Commit and push.

No HTML editing required either way.
