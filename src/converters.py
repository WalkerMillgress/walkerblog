from htmlnode import HTMLNode, LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.NORMAL:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": {text_node.url}})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src": {text_node.url}, "alt": ""})
        case _:
            raise Exception("Not any type of text I recognize, sorry")