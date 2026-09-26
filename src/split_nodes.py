from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        remaining_text = text

        for alt_text, image_url in images:
            image_markdown = f"![{alt_text}]({image_url})"
            sections = remaining_text.split(image_markdown, 1)

            if len(sections) != 2:
                raise ValueError(f"Invalid markdown image syntax: {image_markdown}")
            before_image, after_image = sections

            if before_image:
                new_nodes.append(TextNode(before_image, TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url,))

            remaining_text = after_image

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        remaining_text = text

        for link_text, link_url in links:
            link_markdown = f"[{link_text}]({link_url})"
            sections = remaining_text.split(link_markdown, 1)

            if len(sections) != 2:
                raise ValueError(f"Invalid markdown link syntax: {link_markdown}")

            before_link, after_link = sections

            if before_link:
                new_nodes.append(TextNode(before_link, TextType.TEXT))

            new_nodes.append(
                TextNode(link_text, TextType.LINK, link_url,)
            )
            remaining_text = after_link

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes