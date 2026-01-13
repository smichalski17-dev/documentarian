#!/usr/bin/env python3
"""Simple link checker for the `my-website` folder.

Checks:
- Markdown and HTML links in .md/.mdx/.js/.jsx/.html files
- Relative file links and image paths (exists on disk)
- Image paths under `/img` mapped to `my-website/static/img`
- External HTTP(S) links via simple GET
- Site routes (starting with `/`) are checked against generated .docusaurus JSON permalinks when available

Usage: python tools/link_check.py
"""
import os
import re
import sys
import json
import glob
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / "my-website"

LINK_RE = re.compile(r"\!\[.*?\]\(([^)]+)\)|\[.*?\]\(([^)]+)\)|href=[\"']([^\"']+)[\"']|src=[\"']([^\"']+)[\"']")

def find_files():
    patterns = ["**/*.md", "**/*.mdx", "**/*.html", "**/*.js", "**/*.jsx"]
    files = []
    for p in patterns:
        files.extend(SITE.glob(p))
    return sorted(set(files))

def load_docusaurus_permalinks():
    # scan .docusaurus JSON files for permalinks
    permalinks = set()
    debug_dir = SITE / ".docusaurus"
    if not debug_dir.exists():
        return permalinks
    for j in debug_dir.rglob("*.json"):
        try:
            data = json.loads(j.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            continue
        s = json.dumps(data)
        # quick extract of "/..." strings
        for m in re.findall(r'"(/[^"\\]+)"', s):
            permalinks.add(m)
    return permalinks

def check_external(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent":"link-checker/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return getattr(e, 'code', None)
    except Exception as e:
        return str(e)

def resolve_internal(base_file, link):
    # map /img/... -> my-website/static/img/...
    if link.startswith("/img/"):
        candidate = SITE / "static" / link.lstrip("/")
        return candidate if candidate.exists() else None
    if link.startswith("/"):
        # site route; not a file path
        return None
    # relative path
    candidate = (base_file.parent / link).resolve()
    return candidate if candidate.exists() else None

def extract_links(text):
    links = []
    for m in LINK_RE.finditer(text):
        for g in m.groups():
            if g:
                links.append(g.strip())
                break
    return links

def main():
    files = find_files()
    permalinks = load_docusaurus_permalinks()
    report = {"broken": [], "unverified": []}

    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines, start=1):
            for link in extract_links(line):
                if link.startswith("http://") or link.startswith("https://"):
                    status = check_external(link)
                    if isinstance(status, int) and 200 <= status < 400:
                        continue
                    report["broken"].append({"file": str(f.relative_to(ROOT)), "line": i, "link": link, "reason": f"HTTP {status}"})
                else:
                    resolved = resolve_internal(f, link)
                    if resolved is None:
                        # route or missing; check permalinks for site route
                        if link.startswith("/"):
                            # check route presence
                            if link in permalinks:
                                continue
                            else:
                                report["unverified"].append({"file": str(f.relative_to(ROOT)), "line": i, "link": link, "reason": "site route not found in .docusaurus"})
                        else:
                            report["broken"].append({"file": str(f.relative_to(ROOT)), "line": i, "link": link, "reason": "target file not found"})

    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
