import unittest

from blocktype import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.HEADING,
            block_type,
        )

    def test_heading_levels(self):
        for i in range(1, 7):
            block = "#" * i + " Heading"

            block_type = block_to_block_type(block)

            self.assertEqual(
                BlockType.HEADING,
                block_type,
            )

    def test_invalid_heading(self):
        block = "####### Too many hashes"

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type,
        )

    def test_code(self):
        block = """```
print("Hello")
print("World")
```"""

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.CODE,
            block_type,
        )

    def test_quote(self):
        block = """> This is a quote
> This is another line"""

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.QUOTE,
            block_type,
        )

    def test_invalid_quote(self):
        block = """> This is a quote
This line is not a quote"""

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type,
        )

    def test_unordered_list(self):
        block = """- First item
- Second item
- Third item"""

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.UNORDERED_LIST,
            block_type,
        )

    def test_invalid_unordered_list(self):
        block = """- First item
Second item
- Third item"""

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type,
        )

    def test_ordered_list(self):
        block = """1. First item
2. Second item
3. Third item"""

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.ORDERED_LIST,
            block_type,
        )

    def test_ordered_list_must_start_at_one(self):
        block = """2. First item
3. Second item
4. Third item"""

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type,
        )

    def test_ordered_list_numbers_must_increment(self):
        block = """1. First item
2. Second item
4. Fourth item"""

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type,
        )

    def test_paragraph(self):
        block = "This is just a normal paragraph."

        block_type = block_to_block_type(block)

        self.assertEqual(
            BlockType.PARAGRAPH,
            block_type,
        )


if __name__ == "__main__":
    unittest.main()