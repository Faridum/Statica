import unittest

from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Tolkien Fan Club"
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_extract_title_with_whitespace(self):
        md = "#   Tolkien Fan Club   "
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_extract_title_not_first_line(self):
        md = """
This is some text.

# Tolkien Fan Club

Some more text.
"""
        self.assertEqual(extract_title(md), "Tolkien Fan Club")

    def test_no_title(self):
        md = """
## Blog posts

Some content.
"""

        with self.assertRaises(ValueError):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()