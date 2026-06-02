import os, shutil
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = ROOT_DIR.removesuffix("/src")

def copy_static_into_public(origin="static", target="public",first=True):
    if first:
        public_dir = ROOT_DIR + "/public"
        shutil.rmtree(public_dir)
        os.makedirs(public_dir)
    target_dir = os.path.join(ROOT_DIR, target)
    origin_dir = os.path.join(ROOT_DIR, origin)
    contents = os.listdir(origin_dir)
    for item in contents:
        path_to_item = os.path.join(origin_dir, item)
        path_to_Path = Path(path_to_item)
        if path_to_Path.is_file():
            shutil.copy(path_to_item, target_dir)
        if path_to_Path.is_dir():
            target_dir = os.path.join(target_dir, item)
            os.mkdir(target_dir)
            origin_dir = os.path.join(origin_dir, item)
            copy_static_into_public(origin_dir, target_dir, False)


copy_static_into_public()
