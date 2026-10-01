import unittest

from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
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
        md = "```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = "# This is a heading"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>",
        )

    def test_heading_levels(self):
        md = "### This is a heading"

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h3>This is a heading</h3></div>",
        )

    def test_quote(self):
        md = """
> This is a quote
> with multiple lines
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- First item
- Second item
- Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. First item
2. Second item
3. Third item
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

    def test_mixed_blocks(self):
        md = """
# My Website

This is **my website**.

- Home
- About
- Contact
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>My Website</h1><p>This is <b>my website</b>.</p><ul><li>Home</li><li>About</li><li>Contact</li></ul></div>",
        )


if __name__ == "__main__":
    unittest.main()