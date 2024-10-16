import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.CODE, url="https://www.cnn.com")
        node4 = TextNode("This is a text nOde", TextType.BOLD)
        node5= TextNode("This is a text node", TextType.ITALIC)
        node6 = TextNode("This is a text node", TextType.BOLD, url = None)

        
        self.assertEqual(node, node2)
        

if __name__ == "__main__":
    unittest.main()