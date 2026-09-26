import unittest

from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )

        new_nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image",
                    TextType.IMAGE,
                    "https://i.imgur.com/fJRm4Vk.jpeg",
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode(
                    "link",
                    TextType.LINK,
                    "https://boot.dev",
                ),
            ],
            new_nodes,
        )

    def test_plain_text(self):
        text = "This is just plain text"

        new_nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode(
                    "This is just plain text",
                    TextType.TEXT,
                )
            ],
            new_nodes,
        )

    def test_bold_and_italic(self):
        text = "This is **bold** and _italic_ text"

        new_nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_code(self):
        text = "This is `code`"

        new_nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
            new_nodes,
        )

    def test_image_and_link(self):
        text = (
            "Here is an ![image](image.png) "
            "and [a link](https://example.com)"
        )

        new_nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("Here is an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "image.png",
                ),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "a link",
                    TextType.LINK,
                    "https://example.com",
                ),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()