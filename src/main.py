from copystatic import copy_static_into_public
from gencontent import generate_pages_recursive
import sys

base_path = "/"

if len(sys.argv) > 1 :
    base_path = sys.argv[1]
    
    
copy_static_into_public()

generate_pages_recursive("content", "template.html", "docs", base_path)


