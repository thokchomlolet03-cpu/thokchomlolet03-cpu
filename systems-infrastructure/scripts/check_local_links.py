#!/usr/bin/env python3
"""Validate relative Markdown file links. No network access or dependencies."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import sys

# Backtick fences are removed before scanning to avoid checking examples.
FENCE = re.compile(r"^\s*(" + chr(96) + r"{3,}|~{3,})")
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)\)")


def links_in(text):
    in_fence = None
    for line in text.splitlines():
        fence = FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if in_fence is None:
                in_fence = marker[0]
            elif marker[0] == in_fence:
                in_fence = None
            continue
        if in_fence:
            continue
        for match in LINK.finditer(line):
            yield match.group(1)


def check(root, documents):
    errors = []
    root = root.resolve()
    for doc in documents:
        for link in links_in(doc.read_text(encoding="utf-8")):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (doc.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{doc.relative_to(root)}: link escapes repository: {link}")
            elif not (target.is_file() or (target.is_dir() and (target / "README.md").is_file())):
                errors.append(f"{doc.relative_to(root)}: missing local target: {link}")
    return errors


def main():
    root = Path(__file__).resolve().parents[2]
    docs = sorted((root / "systems-infrastructure").rglob("*.md"))
    docs.append(root / "README.md")
    errors = check(root, docs)
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {len(docs)} Markdown files; {len(errors)} broken relative links.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
