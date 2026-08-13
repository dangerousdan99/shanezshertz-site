"""Generates docs/index.html from collections.json.

Add a new collection by appending an entry to collections.json, then run
this script. No manual HTML editing required. Status is "open" (shows in
the hero CTAs and gets a "Visit the shop" link) or "coming-soon" (shows in
the shop grid only, no link). Adding an 8th, 9th, ... collection needs no
code changes here.
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent
COLLECTIONS = json.loads((ROOT / "collections.json").read_text(encoding="utf-8"))
DOCS = ROOT / "docs"

PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Shanez Shertz</title>
<meta name="description" content="A universe of businesses that take ridiculous ideas completely seriously.">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<header class="site-header">
  <img src="assets/logo.png" alt="Shanez Shertz" class="logo">
</header>

<section class="hero">
  <div class="hero-content">
    <h1>THE MALL IS OPEN.</h1>
    <p class="hero-sub">A universe of businesses that take ridiculous ideas completely seriously. Currently open: {open_names}</p>
    <div class="hero-ctas">
{hero_ctas}
    </div>
  </div>
</section>

<section class="blurb">
  <p>Shanez Shertz isn't one t-shirt brand. It's a mall full of them &mdash; a rejection-letter department, a wellness company that's questionable at best, a gallery that won't explain itself, and more opening soon. Nobody working here finds any of it remarkable.</p>
</section>

<section class="shops">
{shop_cards}
</section>

<footer class="site-footer">
  <div class="social-links">
    <a href="https://www.facebook.com/shanezshertz" aria-label="Facebook">Facebook</a>
    <a href="https://www.instagram.com/shanezshertz/" aria-label="Instagram">Instagram</a>
    <a href="https://tiktok.com/@shanezshertz" aria-label="TikTok">TikTok</a>
  </div>
  <p class="rights">&copy; 2026 Shanez Shertz. All rights reserved.</p>
</footer>

</body>
</html>
"""

CTA_TEMPLATE = '      <a class="cta" href="{redirect}">Shop {name}</a>'

CARD_LIVE_TEMPLATE = """  <div class="shop-card shop-live">
    <h2>{name}</h2>
    <p class="shop-status">Open</p>
    <p>{description}</p>
    <a href="{redirect}">Visit the shop &rarr;</a>
  </div>"""

CARD_SOON_TEMPLATE = """  <div class="shop-card shop-soon">
    <h2>{name}</h2>
    <p class="shop-status">Coming Soon</p>
    <p>{description}</p>
  </div>"""


def build():
    open_collections = [c for c in COLLECTIONS if c["status"] == "open"]
    if not open_collections:
        raise ValueError("at least one collection must have status \"open\"")

    open_names = ", ".join(c["name"] for c in open_collections)
    if not open_names.endswith("."):
        open_names += "."
    hero_ctas = "\n".join(
        CTA_TEMPLATE.format(redirect=c["redirect"], name=c["name"])
        for c in open_collections
    )

    cards = []
    for c in COLLECTIONS:
        if c["status"] == "open":
            cards.append(CARD_LIVE_TEMPLATE.format(**c))
        elif c["status"] == "coming-soon":
            cards.append(CARD_SOON_TEMPLATE.format(**c))
        else:
            raise ValueError(f"unknown status {c['status']!r} for {c['name']!r}")
    shop_cards = "\n".join(cards)

    html = PAGE_TEMPLATE.format(
        open_names=open_names, hero_ctas=hero_ctas, shop_cards=shop_cards
    )
    (DOCS / "index.html").write_text(html, encoding="utf-8")

    print(f"Built docs/index.html: {len(COLLECTIONS)} collections ({len(open_collections)} open)")


if __name__ == "__main__":
    build()
