from copystatic import copy_static_into_public
from gencontent import generate_pages_recursive

copy_static_into_public()

generate_pages_recursive("content", "template.html", "public")


