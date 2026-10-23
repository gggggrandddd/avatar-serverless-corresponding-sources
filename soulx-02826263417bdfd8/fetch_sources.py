#!/usr/bin/env python3
"""Restore original source archive names and verify SHA256. Does not execute sources."""
import hashlib
import json
from pathlib import Path
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
BASE = 'https://github.com/gggggrandddd/avatar-serverless-corresponding-sources/releases/download/soulx-02826263417bdfd8/'
manifest = json.loads((ROOT / 'source-manifest.json').read_text())
for package in manifest['sources']:
    for item in package['files']:
        path = ROOT / item['path']
        if not path.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError('Source destination outside companion directory')
        if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256']:
            continue
        url = BASE + urllib.parse.quote(item['github_asset_name'], safe='')
        with urllib.request.urlopen(url, timeout=120) as response:
            data = response.read()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            raise ValueError('Source archive validation failed: ' + item['github_asset_name'])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        print(path.relative_to(ROOT), flush=True)
