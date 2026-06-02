from copystatic import copy_static_into_public
from gencontent import generate_page

copy_static_into_public()

generate_page("content/index.md", "template.html", "public/index.html")


