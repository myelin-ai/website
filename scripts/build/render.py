import pystache
import htmlmin
from os import path
from datetime import date
import getopt
import sys

PAGES_FOLDER = 'pages'
PUBLIC_FOLDER = 'public'

def render(config, assets):
    with open('template.mustache') as f:
        template = f.read()

    for person in config['people']:
        if 'image' in person:
            person['image_url'] = assets[person['image']]

    for page in config['pages']:
        page_file = path.join(PAGES_FOLDER, page['file'] + '.mustache')

        with open(page_file) as f:
            page_template = f.read()

        nav = []
        for nav_page in config['pages']:
            if 'path' in nav_page:
                is_active = False

                if 'path' in page:
                    is_active = (nav_page['path'] == page['path'])

                nav.append({
                    'path': nav_page['path'],
                    'title': nav_page['title'],
                    'is_active': is_active,
                })

        if 'title' in page:
            title = page['title'] + ' · ' + config['title']
        else:
            title = config['title']

        context = {
            'nav': nav,
            'config': config,
            'page': page,
            'page_file': page_file,
            'title': title,
            'year': date.today().year,
            'people': config['people'],
            'assets': assets,
        }

        context['content'] = pystache.render(page_template, context)

        page_html = htmlmin.minify(
            pystache.render(template, context),
            remove_optional_attribute_quotes=False,
            remove_empty_space=True,
        )

        with open(path.join(PUBLIC_FOLDER, page['file'] + '.html'), 'w') as f:
            f.write(page_html)
