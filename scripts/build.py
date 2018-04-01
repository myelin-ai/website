#!/usr/bin/env python3
import toml
from build import render, build_assets

with open('config.toml') as f:
    config = toml.loads(f.read())

render(config, build_assets(config))
