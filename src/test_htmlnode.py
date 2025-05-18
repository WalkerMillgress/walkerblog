import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode()
        print(node)

    def test_print(self):
        node = HTMLNode("div", None, None, {"href": "mateo.com", "target": "_blank"})
        print(node.props_to_html())

    def test_toHTML(self):
        node = LeafNode("p", "Hello, world!")
        print(node.to_html())

if __name__ == "__main__":
    unittest.main()