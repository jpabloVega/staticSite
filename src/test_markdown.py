import unittest
from markdown_delimiter import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class TestMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_blocks_to_block_type_heading(self):
        markdown = "### Hello"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_blocks_to_block_type_code(self):
        markdown = """```
this is a code block
```"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.CODE)

    def test_blocks_to_block_type_quote(self):
        markdown = """>im a quote
> veryquote
>  manyquotealso"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_blocks_to_block_type_unordered(self):
        markdown = """- first
- second
- third"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.UN_LIST)

    def test_blocks_to_block_type_heading(self):
        markdown = """1.first
    2.second
    3.third"""
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.OR_LIST)

    def test_blocks_to_block_type_heading(self):
        markdown = "Im just a normal paragraph"
        block_type = block_to_block_type(markdown)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )