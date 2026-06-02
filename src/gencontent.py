from markdown_delimiter import markdown_to_html_node
from copystatic import ROOT_DIR
from pathlib import Path
import os, shutil

def extract_title(markdown) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if not line:
            continue
        if line[0] == "#" and line[1] != "#":
            result = line.removeprefix("#")
            return result.strip()
    raise Exception("There is no valid title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    open_md = open(from_path, "r", encoding="utf-8")
    md_cont = open_md.read()
    open_cont = open(template_path, "r", encoding="utf-8")
    temp_cont = open_cont.read()
    html_node = markdown_to_html_node(md_cont)
    contents = html_node.to_html()
    title = extract_title(md_cont)
    temp_cont = temp_cont.replace("{{ Title }}", title)
    temp_cont = temp_cont.replace("{{ Content }}", contents)
    file_path = Path(os.path.join(ROOT_DIR, dest_path))
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(temp_cont)
    open_md.close()
    open_cont.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dir = os.path.join(ROOT_DIR, dir_path_content)
    content_contents = os.listdir(content_dir)
    dest_path = os.path.join(ROOT_DIR, dest_dir_path)
    for item in content_contents:
        path_to_item = os.path.join(content_dir, item)
        path_to_Path = Path(path_to_item)
        if path_to_Path.is_file():
            if path_to_Path.suffix == ".md":
                dest_html = os.path.join(dest_path, "index.html")
                generate_page(path_to_item, template_path, dest_html)
            else:
                pass
        elif path_to_Path.is_dir():
            path_to_dir = os.path.join(dest_path, item)
            generate_pages_recursive(path_to_item, template_path, path_to_dir)

    