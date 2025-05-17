import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_links(self):
        node = TextNode("this is something", TextType.LINK, "joder.com")
        node2 = TextNode("this is something", TextType.LINK, "joder.com")
        self.assertEqual(node, node2)

    def test_dif(self):
        node = TextNode("this is something", TextType.LINK, "joder.com2")
        node2 = TextNode("this is something", TextType.LINK, "joder.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()