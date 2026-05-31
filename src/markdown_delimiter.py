from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from delimiter import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UN_LIST = "unordered list"
    OR_LIST = "ordered list"

def block_to_block_type(block) -> BlockType:
    lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UN_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OR_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown) -> list:
    filtered_blocks = []
    blocks = markdown.split("\n\n")
    for item in blocks:
        filtered_item = item.strip()
        if filtered_item == "":
            continue
        filtered_blocks.append(filtered_item)
    return filtered_blocks

def text_to_children(text) -> list:
    child_text_nodes = text_to_textnodes(text)
    children_list =[]
    for child in child_text_nodes:
        new_child = text_node_to_html_node(child)
        children_list.append(new_child)
    return children_list

def blocks_to_html_node(block) -> ParentNode:
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html(block)
    if block_type == BlockType.HEADING:
        return heading_to_html(block)
    if block_type == BlockType.CODE:
        return code_to_html(block)
    if block_type == BlockType.OR_LIST:
        return or_list_to_html(block)
    if block_type == BlockType.UN_LIST:
        return un_list_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    raise ValueError("invalid block type")

def paragraph_to_html(block) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html(block) -> ParentNode:
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html(block) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def or_list_to_html(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def un_list_to_html(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html(block: str) -> ParentNode:
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def markdown_to_html_node(markdown) ->  ParentNode:
    blocks = markdown_to_blocks(markdown)
    parent_blocks = []
    for block in blocks:
        html_node = blocks_to_html_node(block)
        parent_blocks.append(html_node)
    return ParentNode("div", parent_blocks, None)

    





