from textnode import TextNode, TextType, text_node_to_html_node
from delimiter import extract_markdown_images, extract_markdown_links, split_nodes_link, text_to_textnodes
from markdown_delimiter import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node, text_to_children

md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

html_node = markdown_to_html_node(md)
result = html_node.to_html()

print(result)
