import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_same_value(self):
        node = HTMLNode("p", "Hello this is a test")
        node2 = HTMLNode("p", "Hello this is a test")
        self.assertEqual(node.value, node2.value)

    def test_not_eq_value(self):
        node = HTMLNode("p", "Hello this is a test")
        node2 = HTMLNode("h1", "Hello this is a different test")
        self.assertNotEqual(node.value, node2.value)

    def test_same_tag(self):
        node = HTMLNode("p", "Hello this is a test")
        node2 = HTMLNode("p", "Hello this is a test")
        self.assertEqual(node.tag, node2.tag)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click Me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_many_children(self):
        child1 = LeafNode("h1", "First child")
        child2 = LeafNode("b", "Second child")
        child3 = LeafNode("span", "Last child")
        parent_node = ParentNode("div", [child1, child2, child3])
        self.assertEqual(
            parent_node.to_html(),
            "<div><h1>First child</h1><b>Second child</b><span>Last child</span></div>"
        )