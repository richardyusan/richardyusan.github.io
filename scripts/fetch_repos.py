#!/usr/bin/env python3
"""Fetch all public repositories of a GitHub user into _data/repos.json.

Run by .github/workflows/jekyll.yml before every build (on push, on a
schedule, and on demand), so the Projects page always mirrors GitHub.

Usage: python scripts/fetch_repos.py <github-user> [output-path]
Set GITHUB_TOKEN to avoid the unauthenticated rate limit.
"""
import json
import os
import sys
import urllib.request

FIELDS = [
    "name", "full_name", "description", "html_url", "homepage", "language",
    "stargazers_count", "forks_count", "topics", "fork", "archived",
    "created_at", "updated_at", "pushed_at",
]
# Repos that should never be listed (e.g. this site itself).
SKIP = {"richardyusan.github.io"}


def fetch(user):
    repos, page = [], 1
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "repo-sync"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    while True:
        url = (f"https://api.github.com/users/{user}/repos"
               f"?per_page=100&page={page}&type=owner&sort=pushed")
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as r:
            batch = json.load(r)
        if not batch:
            return repos
        repos.extend(batch)
        page += 1


def main():
    user = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "_data/repos.json"
    repos = [
        {k: r.get(k) for k in FIELDS}
        for r in fetch(user)
        if not r.get("private") and r["name"] not in SKIP
    ]
    repos.sort(key=lambda r: r["pushed_at"] or "", reverse=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(repos)} repositories to {out}")


if __name__ == "__main__":
    main()
