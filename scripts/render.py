#!/usr/bin/env python3
import toml
import pystache
import htmlmin
from os import path
from datetime import date
import getopt
import sys

PAGES_FOLDER = 'pages'
PUBLIC_FOLDER = 'public'

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["css-file="])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

css_file = 'style.css'

for opt, val in opts:
    if opt == '--css-file':
        css_file = val

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
        'people': config['people'],
        'css_file': css_file,
    }

    context['content'] = pystache.render(page_template, context)

    page_html = htmlmin.minify(
        pystache.render(template, context),
        remove_optional_attribute_quotes=False,
        remove_empty_space=True,
    )

    with open(path.join(PUBLIC_FOLDER, page['file'] + '.html'), 'w') as f:
        f.write(page_html)
