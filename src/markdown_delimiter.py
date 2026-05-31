from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from delimiter import text_to_textnodes
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UN_LIST = "unordered list"
    OR_LIST = "ordered list"

def block_to_block_type(markdown) -> BlockType:
    every_line = markdown.split("\n")
    if markdown[0] == "#":
        return BlockType.HEADING
    if markdown[0:4] == "```\n" and markdown[-3:] == "```":
        return BlockType.CODE
    for i in range(len(every_line)):
        line = every_line[i]
        if line[0] != ">":
            break
        if i == len(every_line)-1 and line[0] == ">":
            return BlockType.QUOTE
    for i in range(len(every_line)):
        line = every_line[i]
        if line[0:2] != "- ":
            break
        if i == len(every_line)-1 and line[0:2] == "- ":
            return BlockType.UN_LIST
    for i in range(len(every_line)):
        line = every_line[i]
        if i == 0:
            num = 1
        if line[0:2] != f"{num}.":
            break
        if i == len(every_line)-1 and line[0:2] == f"{num}.":
            return BlockType.OR_LIST
        num += 1
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

def markdown_get_html_tag(BlockType) -> str:
    if BlockType == BlockType.PARAGRAPH:
        return "p"
    if BlockType == BlockType.HEADING:
        return "h1"
    if BlockType == BlockType.CODE:
        return "```"
    if BlockType == BlockType.QUOTE:
        return "blockquote"
    if BlockType == BlockType.UN_LIST:
        return "ul"
    if BlockType == BlockType.OR_LIST:
        return "ol"

def text_to_children(text) -> list:
    child_text_nodes = text_to_textnodes(text)
    children_list =[]
    for child in child_text_nodes:
        new_child = text_node_to_html_node(child)
        children_list.append(new_child)
    return children_list

def markdown_to_html_node(markdown) ->  HTMLNode:
    blocks = markdown_to_blocks(markdown)
    parent_blocks = []
    for block in blocks:
        type = block_to_block_type(block)
        tag = markdown_get_html_tag(type)
        children = text_to_textnodes(block)
        parent_node = ParentNode(tag, children)
        parent_blocks.append(parent_node)
    complete_block = ParentNode("div", parent_blocks)
    return complete_block.to_html()





