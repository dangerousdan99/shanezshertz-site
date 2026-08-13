# shanezshertz-site

The Shanez Shertz homepage, live at `shanezshertz.shop`. A static one-pager — no build step in the shipped page (no JS, no framework), but the HTML itself is generated from data.

## Structure

- `collections.json` — one entry per collection: `slug`, `name`, `status` (`"open"` or `"coming-soon"`), `description`, and `redirect` (required only when `status` is `"open"`).
- `build.py` — reads `collections.json`, writes `docs/index.html`. Run `python build.py` after editing `collections.json`.
- `docs/` — served by GitHub Pages (custom domain via `docs/CNAME`).
- `docs/styles.css` — all styling (grid-based shop cards and flex-wrapped hero CTAs already scale to any number of collections, no CSS changes needed to add more).
- `docs/assets/` — logo and hero banner.
- `docs/404.html` — hand-written, not generated.

## Adding a collection

1. Append an entry to `collections.json` (status `"coming-soon"`, no `redirect` yet).
2. Run `python build.py`.
3. Commit and push.

## Launching a collection that's already "coming-soon"

1. In `collections.json`, change its `status` to `"open"` and add its `redirect` (the `go.shanezshertz.shop/<slug>` collection-level redirect — set that up in `shanezshertz-go` first).
2. Run `python build.py`.
3. Commit and push.

No HTML editing required either way.
