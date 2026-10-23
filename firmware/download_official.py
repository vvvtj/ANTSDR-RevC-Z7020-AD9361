#!/usr/bin/env python3
"""List/download official ANTSDR firmware GitHub release assets; NEVER flash.
Uses Python standard library only.
"""
import argparse
import hashlib
import json
import pathlib
import urllib.request

REPOS = ["MicroPhase/antsdr-fw", "MicroPhase/antsdr-fw-patch"]
ROOT = pathlib.Path(__file__).resolve().parent / "releases"
HEADERS = {"User-Agent": "ANTSDR-E310-RevC-archive/1.0",
           "Accept": "application/vnd.github+json"}

def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()

def releases(repo):
    page = 1
    while True:
        result = json.loads(get(f"https://api.github.com/repos/{repo}/releases?per_page=100&page={page}"))
        if not result:
            break
        for release in result:
            yield release
        page += 1

def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--list", action="store_true")
    g.add_argument("--download", action="store_true")
    args = p.parse_args()
    for repo in REPOS:
        for release in releases(repo):
            tag = release["tag_name"]
            print(f"{repo}: {tag}")
            for asset in release.get("assets", []):
                name, url = asset["name"], asset["browser_download_url"]
                print(f"  {name} ({asset['size']} bytes) {url}")
                if not args.download:
                    continue
                destdir = ROOT / repo.replace("/", "_") / tag
                destdir.mkdir(parents=True, exist_ok=True)
                dest = destdir / pathlib.Path(name).name
                if dest.exists() and dest.stat().st_size == asset["size"]:
                    print("   exists, skipped")
                    continue
                payload = get(url)
                if len(payload) != asset["size"]:
                    raise RuntimeError(f"Download size mismatch for {url}")
                dest.write_bytes(payload)
                digest = hashlib.sha256(payload).hexdigest()
                (destdir / (dest.name + ".sha256")).write_text(f"{digest}  {dest.name}\n")
                print(f"   saved {dest} sha256={digest}")
if __name__ == "__main__":
    main()
