# sgc4e.github.io

Saurabh Garg's "Built on GitHub" page: every repo since 14 February 2025, one card each.

- `index.html` reads `projects.json` (only the cards switched on).
- `admin.html` edits cards and toggles them. Needs a fine-grained token with Contents read/write on this repo and on the private `sgc4e/github-showcase-data`, plus Metadata read on all repos. Save writes the full list to the private repo and the shown cards here.
- Hidden cards never reach this public repo.
