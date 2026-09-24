import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")],matches,)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://example.com)")
        self.assertListEqual([("link", "https://example.com")],matches,)

    def test_extract_markdown_links_with_exclamation(self):
        matches = extract_markdown_links("This is text with a ![link](https://example.com)")
        self.assertListEqual([], matches)

    def test_extract_multiple_images(self):
        matches = extract_markdown_images("![image1](https://example.com/1.png) ""and ![image2](https://example.com/2.png)")
        self.assertListEqual([("image1", "https://example.com/1.png"),("image2", "https://example.com/2.png"),],matches,)

    def test_extract_multiple_links(self):
        matches = extract_markdown_links("Visit [Google](https://google.com) " "or [GitHub](https://github.com)")
        self.assertListEqual([("Google", "https://google.com"),("GitHub", "https://github.com"),],matches,)

    def test_extract_no_images(self):
        matches = extract_markdown_images("This text contains no images.")
        self.assertListEqual([], matches)

    def test_extract_no_links(self):
        matches = extract_markdown_links("This text contains no links.")
        self.assertListEqual([], matches)

    def test_extract_mixed_links_and_images(self):
        text = ("Here is [a link](https://example.com) " "and here is ![an image](https://example.com/image.png)")
        links = extract_markdown_links(text)
        images = extract_markdown_images(text)

        self.assertListEqual([("a link", "https://example.com")],links,)

        self.assertListEqual([("an image", "https://example.com/image.png")],images,)
