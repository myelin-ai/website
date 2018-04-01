from os import path
import hashlib
import sys
import shutil

PUBLIC_FOLDER = 'public'
ASSETS_FOLDER = 'assets'
STATIC_FOLDER = 'static'
BUF_SIZE = 65536

def hash_file(path):
    sha1 = hashlib.sha1()

    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)

            if not data:
                break

            sha1.update(data)
    
    return sha1.hexdigest()[:10]

def build_assets(config):
    assets = {}

    for asset in config['assets']:
        name = asset['name']
        source = asset['source']
        filename, ext = path.splitext(source)

        asset_path = path.join(ASSETS_FOLDER, source)
        file_hash = hash_file(asset_path)

        filename_with_hash = path.basename(filename) + '-' + file_hash + ext
        
        assets[name] = '/' + STATIC_FOLDER + '/' + filename_with_hash

        shutil.copy(
            asset_path,
            path.join(PUBLIC_FOLDER, STATIC_FOLDER, filename_with_hash)
        )

    return assets
