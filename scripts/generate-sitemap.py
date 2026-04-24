#!/usr/bin/env python3
"""Update sitemap.ts by scanning src/content/blog/ for markdown files."""
import os
import re
import json
from datetime import datetime, timezone
import glob

BASE_URL = "https://chanblog.xyz"
PROJECT_DIR = "/mnt/d/project/Chan-s-Blogs"
CONTENT_DIR = os.path.join(PROJECT_DIR, "src/content")
SITEMAP_PATH = os.path.join(PROJECT_DIR, "src/app/sitemap.ts")


def parse_frontmatter(filepath):
    """Simple frontmatter parser without gray-matter dependency."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Match YAML frontmatter between --- markers
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    
    yaml_text = match.group(1)
    data = {}
    
    # Parse simple YAML fields
    for line in yaml_text.split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            # Remove quotes
            value = value.strip('"').strip("'")
            data[key] = value
    
    return data


def get_priority(url_path):
    if url_path in ("/", ""):
        return 1.0
    if url_path == "blog":
        return 0.9
    return 0.8


def get_change_frequency(url_path):
    if url_path in ("/", "", "blog"):
        return "daily"
    return "weekly"


def scan_markdown_files(directory):
    """Recursively scan markdown files."""
    items = []
    
    for root, dirs, files in os.walk(directory):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue
            
            filepath = os.path.join(root, fname)
            data = parse_frontmatter(filepath)
            
            # Get relative path from src/content/
            rel_path = os.path.relpath(root, CONTENT_DIR)
            url_path = os.path.join(rel_path, fname.replace(".md", "")).replace("\\", "/")
            
            last_modified = data.get("updated", datetime.now(timezone.utc).isoformat())
            
            items.append({
                "url": url_path,
                "lastModified": last_modified,
                "changeFrequency": get_change_frequency(url_path),
                "priority": get_priority(url_path)
            })
    
    return items


def generate_sitemap():
    items = scan_markdown_files(CONTENT_DIR)
    
    # Add root and /blog pages
    items.insert(0, {
        "url": "/",
        "lastModified": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "changeFrequency": "daily",
        "priority": 1.0
    })
    items.insert(1, {
        "url": "/blog",
        "lastModified": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "changeFrequency": "daily",
        "priority": 0.9
    })
    
    # Build TypeScript content
    items_json = json.dumps(items, indent=2, ensure_ascii=False)
    # Replace "lastModified": "ISO" with lastModified: new Date("ISO")
    items_json = re.sub(
        r'"lastModified": "([^"]+)"',
        r'lastModified: new Date("\1")',
        items_json
    )
    
    ts_content = f"""import type {{ MetadataRoute }} from 'next'

export default function sitemap(): MetadataRoute.Sitemap {{
  return {items_json}
}}
"""
    
    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(ts_content)
    
    print(f"✅ Generated sitemap with {len(items)} items → {SITEMAP_PATH}")


if __name__ == "__main__":
    generate_sitemap()
