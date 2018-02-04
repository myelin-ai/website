#!/usr/bin/env python3
import toml
import pystache
from os import path
from datetime import date

PAGES_FOLDER = 'pages'
PUBLIC_FOLDER = 'public'

with open('config.toml') as f:
    config = toml.loads(f.read())

with open('template.mustache') as f:
    template = f.read()

for page in config['pages']:
    page_file = path.join(PAGES_FOLDER, page['file'] + '.mustache')

    with open(page_file) as f:
        page_template = f.read()

    nav = []
    for nav_page in config['pages']:
        if 'title' in nav_page:
            nav.append({
                'path': nav_page['path'],
                'title': nav_page['title'],
                'is_active': nav_page['path'] == page['path'],
            })

    if 'title' in page:
        title = page['title'] + ' · ' + config['title']
    else:
        title = config['title']

    context = {
        'nav': nav,
        'config': config,
        'page': page,
        'title': title,
        'year': date.today().year,
    }

    context['content'] = pystache.render(page_template, context)

    page_html = pystache.render(template, context)

    with open(path.join(PUBLIC_FOLDER, page['file'] + '.html'), 'w') as f:
        f.write(page_html)
