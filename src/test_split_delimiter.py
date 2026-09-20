import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        node = TextNode(
            "This is text with a `code block` word",
            TextType.TEXT,
        )

        result = split_nodes_delimiter(
            [node],
            "`",
            TextType.CODE,
        )

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_bold(self):
        node = TextNode(
            "This is **bold** text",
            TextType.TEXT,
        )

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD,
        )

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_italic(self):
        node = TextNode(
            "This is _italic_ text",
            TextType.TEXT,
        )

        result = split_nodes_delimiter(
            [node],
            "_",
            TextType.ITALIC,
        )

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]

        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        node = TextNode("This is plain text", TextType.TEXT)

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD,
        )

        self.assertEqual(result, [node])

    def test_already_formatted_node(self):
        node = TextNode("already bold", TextType.BOLD)

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD,
        )

        self.assertEqual(result, [node])

    def test_multiple_delimiters(self):
        node = TextNode(
            "Hello **world** and **everyone**",
            TextType.TEXT,
        )

        result = split_nodes_delimiter(
            [node],
            "**",
            TextType.BOLD,
        )

        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("everyone", TextType.BOLD),
        ]

        self.assertEqual(result, expected)

    def test_unclosed_delimiter(self):
        node = TextNode(
            "This is **bold text",
            TextType.TEXT,
        )

        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD,
            )


if __name__ == "__main__":
    unittest.main()