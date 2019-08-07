"""Tests for huffman.py."""
import unittest
from .huffman import HuffmanTree, Node

class TestHuffman(unittest.TestCase):

    def test_generate_tree_from_keys(self):
        keys = {
            'A': 0,
            'B': 111,
            'C': 1100,
            'D': 1101,
            'R': 10,
        }
        correct_tree = Node(
                l_child= Node(characters='A'),
                r_child= Node(
                    l_child= Node(characters='R'),
                    r_child= Node(
                        l_child= Node(
                            l_child= Node(characters='C'),
                            r_child= Node(characters='D'),
                        ),
                        r_child= Node(characters='B')
                    ),     
                ),
            )
        root = HuffmanTree('').generate_tree_from_keys(keys)
        self.assertEqual(root, correct_tree)

if __name__ == '__main__':
    unittest.main()          