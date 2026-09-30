from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    # Heading
    if block.startswith("#"):
        heading_end = block.find(" ")

        if 1 <= heading_end <= 6:
            return BlockType.HEADING

    # Code
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    # Quote
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list
    ordered_list = True

    for i, line in enumerate(lines):
        expected_prefix = f"{i + 1}. "

        if not line.startswith(expected_prefix):
            ordered_list = False
            break

    if ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH