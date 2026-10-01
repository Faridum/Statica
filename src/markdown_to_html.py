from htmlnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type


def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)

    return [
        text_node_to_html_node(text_node)
        for text_node in text_nodes
    ]


def paragraph_to_html_node(block: str):
    lines = block.split("\n")
    text = " ".join(lines)

    children = text_to_children(text)

    return ParentNode("p", children)


def heading_to_html_node(block: str):
    space_index = block.find(" ")
    heading_level = space_index

    text = block[space_index + 1:]

    children = text_to_children(text)

    return ParentNode(
        f"h{heading_level}",
        children,
    )


def quote_to_html_node(block: str):
    lines = block.split("\n")

    text = " ".join(
        line[1:].lstrip()
        for line in lines
    )

    children = text_to_children(text)

    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block: str):
    lines = block.split("\n")

    list_items = []

    for line in lines:
        text = line[2:]
        children = text_to_children(text)

        list_items.append(
            ParentNode("li", children)
        )

    return ParentNode("ul", list_items)


def ordered_list_to_html_node(block: str):
    lines = block.split("\n")

    list_items = []

    for line in lines:
        text = line.split(". ", 1)[1]
        children = text_to_children(text)

        list_items.append(
            ParentNode("li", children)
        )

    return ParentNode("ol", list_items)


def code_to_html_node(block: str):
    code = block[4:-3]

    text_node = TextNode(code, TextType.TEXT)

    code_node = text_node_to_html_node(text_node)

    return ParentNode(
        "pre",
        [
            ParentNode(
                "code",
                [code_node],
            )
        ],
    )


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)

    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block_node = paragraph_to_html_node(block)

        elif block_type == BlockType.HEADING:
            block_node = heading_to_html_node(block)

        elif block_type == BlockType.CODE:
            block_node = code_to_html_node(block)

        elif block_type == BlockType.QUOTE:
            block_node = quote_to_html_node(block)

        elif block_type == BlockType.UNORDERED_LIST:
            block_node = unordered_list_to_html_node(block)

        elif block_type == BlockType.ORDERED_LIST:
            block_node = ordered_list_to_html_node(block)

        else:
            raise ValueError(
                f"Unsupported block type: {block_type}"
            )

        block_nodes.append(block_node)

    return ParentNode("div", block_nodes)