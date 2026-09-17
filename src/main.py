from textnode import TextNode, TextType

def main():
    node1 = TextNode("Hello, World!", TextType.PLAIN_TEXT)
    node2 = TextNode("Hello, World!", TextType.PLAIN_TEXT)
    print(node1 == node2)
    print(node1)

main()