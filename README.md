# richardyusan.github.io

Personal site of Richard Yusan, built on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template.

## How the project list stays in sync

- `.github/workflows/jekyll.yml` runs `scripts/fetch_repos.py` before every build. It writes all public repos to `_data/repos.json`.
- The workflow runs on every push, every 6 hours, and on demand (**Actions → Deploy → Run workflow**).
- `_includes/repo-cards.html` renders that data. In the browser it also refreshes live from the GitHub API, so a new repo shows up right away.
- To hide a repo, add its name to `SKIP` in `scripts/fetch_repos.py`.

## Editing

- Sidebar / site info: `_config.yml`
- Home page: `_pages/about.md`
- CV: `_pages/cv.md`
- Menu: `_data/navigation.yml`
- Publications, talks, teaching, blog: add Markdown files to `_publications/`, `_talks/`, `_teaching/`, `_posts/`. Then add the page back to the menu.
