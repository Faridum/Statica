import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://i.imgur.com/zjjcJKZ.png",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image",
                    TextType.IMAGE,
                    "https://i.imgur.com/3elNhQu.png",
                ),
            ],
            new_nodes,
        )

    def test_split_image_at_beginning(self):
        node = TextNode(
            "![image](https://example.com/image.png) after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://example.com/image.png",
                ),
                TextNode(" after", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_at_end(self):
        node = TextNode(
            "before ![image](https://example.com/image.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("before ", TextType.TEXT),
                TextNode(
                    "image",
                    TextType.IMAGE,
                    "https://example.com/image.png",
                ),
            ],
            new_nodes,
        )

    def test_split_images_with_no_images(self):
        node = TextNode(
            "This text has no images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "This text has no images",
                    TextType.TEXT,
                )
            ],
            new_nodes,
        )

    def test_split_images_preserves_non_text_nodes(self):
        node = TextNode(
            "image",
            TextType.IMAGE,
            "https://example.com/image.png",
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [node],
            new_nodes,
        )


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.boot.dev) and another [link](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode(
                    "link",
                    TextType.LINK,
                    "https://www.boot.dev",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "link",
                    TextType.LINK,
                    "https://www.youtube.com/@bootdotdev",
                ),
            ],
            new_nodes,
        )

    def test_split_link_at_beginning(self):
        node = TextNode(
            "[Google](https://google.com) is a search engine",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "Google",
                    TextType.LINK,
                    "https://google.com",
                ),
                TextNode(
                    " is a search engine",
                    TextType.TEXT,
                ),
            ],
            new_nodes,
        )

    def test_split_link_at_end(self):
        node = TextNode(
            "Visit [Google](https://google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Visit ", TextType.TEXT),
                TextNode(
                    "Google",
                    TextType.LINK,
                    "https://google.com",
                ),
            ],
            new_nodes,
        )

    def test_split_links_with_no_links(self):
        node = TextNode(
            "This text has no links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "This text has no links",
                    TextType.TEXT,
                )
            ],
            new_nodes,
        )

    def test_split_links_preserves_non_text_nodes(self):
        node = TextNode(
            "image",
            TextType.IMAGE,
            "https://example.com/image.png",
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [node],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()