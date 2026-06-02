from markdown_delimiter import markdown_to_html_node
from copystatic import ROOT_DIR
from pathlib import Path
import os

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
    md_cont = open(from_path, "r", encoding="utf-8").read()
    temp_cont = open(template_path, "r", encoding="utf-8").read()
    html_node = markdown_to_html_node(md_cont)
    contents = html_node.to_html()
    title = extract_title(md_cont)
    temp_cont = temp_cont.replace("{{ Title }}", title)
    temp_cont = temp_cont.replace("{{ Content }}", contents)
    file_path = Path(os.path.join(ROOT_DIR, dest_path))
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(temp_cont)
    