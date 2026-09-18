import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"class": "link"})
        result = node.props_to_html()
        self.assertEqual(result, 'class="link"')

    def test_not_eq(self):
        expected = HTMLNode(props={"class": "link"})
        actual = HTMLNode(props={"class": "button"})
        self.assertNotEqual(expected.props_to_html(), actual.props_to_html())

    def test_blank(self):
        expected = HTMLNode(props={"class": "link"})
        actual = HTMLNode(props={})
        self.assertNotEqual(expected.props_to_html(), actual.props_to_html())

    def test_blank_props(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, '')