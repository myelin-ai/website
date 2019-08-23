#!/usr/bin/env python3

import tempfile
import subprocess
from typing import List
import os
import shutil

TEMP_DIR = tempfile.mkdtemp()
TARGET_BRANCH = 'gh-pages'
PUBLIC_DIR = 'public'
BOT_USER = 'myelin-bot'

def _copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def _run_git_command(args: List[str]):
    subprocess.check_call(['git', '-C', TEMP_DIR, *args])

def _get_remote_url() -> str:
    github_token = os.environ['GITHUB_TOKEN']
    repository = os.environ['GITHUB_REPOSITORY']
    return f'https://{BOT_USER}:{github_token}@github.com/{repository}'
    
def _clone_repository():
    subprocess.check_call(['git', 'clone', _get_remote_url(), '--quiet', '-b', TARGET_BRANCH, TEMP_DIR])

def _remove_all_files():
    _run_git_command(['rm', '-r', '.'])

def _copy_files_to_repository():
    _copytree(PUBLIC_DIR, TEMP_DIR)

def _commit_all_changes():
    commit = os.environ['GITHUB_SHA']
    _run_git_command(['add', '-A'])
    _run_git_command(['commit', '--allow-empty', '-m', f'Build for {commit}'])

def _push():
    _run_git_command(['push'])

try:
    print(TEMP_DIR)
    _clone_repository()
    _remove_all_files()
    _copy_files_to_repository()
    _commit_all_changes()
    _push()
finally:
    shutil.rmtree(TEMP_DIR)
