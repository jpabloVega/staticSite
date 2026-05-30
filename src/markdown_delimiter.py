from enum import Enum

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

def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")
    for item in blocks:
        filtered_item = item.strip()
        if filtered_item == "":
            continue
        filtered_blocks.append(filtered_item)
    return filtered_blocks
