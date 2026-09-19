import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
  
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_span_with_props(self):
        node = LeafNode("span", "Hello, world!", props={"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Hello, world!</span>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tag_no_value(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_with_multiple_props(self):
        node = LeafNode("div", "Content", props={"id": "main", "class": "container"})
        self.assertEqual(node.to_html(), '<div id="main" class="container">Content</div>')