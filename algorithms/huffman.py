"""Huffman's algorithm."""
# import utils
from . import utils
import dataclasses
from .compressed_file import CompressedFile
from .algorithm import Algorithm


class Node():
    """Huffman node."""

    def __init__(self, l_child=None, r_child=None, characters=None, weight=None):
        """Init."""
        self.characters = characters
        self.weight = weight
        self.l_child = l_child
        self.r_child = r_child

    def __contains__(self, key):
        """Override contain."""
        return key == self.characters

    def __gt__(self, other):
        """Override greater than."""
        if self.weight > other.weight:
            return True
        else:
            return False

    def __lt__(self, other):
        """Override less than."""
        if self.weight < other.weight:
            return True
        else:
            return False

    # def __eq__(self, other):
    #     """Override equal."""
    #     if self.weight == other.weight:
    #         return True
    #     else:
    #         return False


class HuffmanTree():
    """Huffman tree."""

    def __init__(self, data):
        """Init."""
        try:
            self.data = data.decode('utf-8')
        except AttributeError as e:
            self.data = data
        self.nodes = []
        self.key = {}

    def order_object(self):
        """Orders my tree."""
        pass

    def char_in_nodes(self, char):
        for idx, node in enumerate(self.nodes):
            if char in node:
                return idx
        return -1

    def get_inital_weights(self):
        """Get the list of characters for a weighted dictionary."""
        for character in self.data:
            index = self.char_in_nodes(character)
            if index >= 0:
                self.nodes[index] = Node(characters=character, weight=self.nodes[index].weight+1)
            else:
                self.nodes.append(Node(characters=character, weight=1))
        self.nodes.sort(key=lambda x: x.weight)

    def huff(self, node_1, node_2):
        combined_weight = node_1.weight + node_2.weight
        if node_1 > node_2:
            combined_characters = node_2.characters + node_1.characters
            new_node = Node(
                characters=combined_characters,
                weight=combined_weight,
                r_child=node_1,
                l_child=node_2
            )
        else:
            combined_characters = node_1.characters + node_2.characters
            new_node = Node(
                characters=combined_characters,
                weight=combined_weight,
                r_child=node_2,
                l_child=node_1
            )
        self.nodes.append(new_node)
        self.nodes.pop(0)
        self.nodes.pop(0)
        self.nodes.sort(key=lambda x: x.weight)

    def generate_tree(self):
        """Generate the tree/order."""
        while len(self.nodes) > 1:
            self.huff(self.nodes[0], self.nodes[1])

    def get_key(self, node, key_string):
        """Get the key mf."""
        if not node.r_child and not node.l_child:
            self.key[node.characters] = key_string
        if node.l_child:
            self.get_key(node.l_child, key_string + '0')
        if node.r_child:
            self.get_key(node.r_child, key_string + '1')

    def yeehaw(self):
        output = ''
        for character in self.data:
            output += self.key[character]
        return str.encode(output)

    def generate_tree_from_keys(self, keys_dict):
        root = Node()
        current_node = root
        for key in keys_dict.keys():
            binary_value = keys_dict[key]
            for val in binary_value:
                if (val == '0'):
                    if (current_node.l_child == None):
                        current_node.l_child = Node()
                    current_node = current_node.l_child
                elif (val == '1'):
                    if (current_node.r_child == None):
                        current_node.r_child = Node()
                    current_node = current_node.r_child
            current_node.characters = key
            current_node = root
        # root = self.generate_chars(root)
        return root

    def generate_chars(self, root):
        # if (root.l_child == None and root.r_child == None):
        #     return root.characters
        if (root.characters == None):
            root.characters = self.generate_chars(root.l_child) + self.generate_chars(root.r_child)
        return root.characters


class Huffman(Algorithm):
    """Copy data directly, no actual compression."""

    def compress(self, metadata):
        """Compress function for Huffman's algorithm."""
        data = utils.read(metadata.input_path)
        tree = HuffmanTree(data)
        tree.get_inital_weights()
        tree.generate_tree()
        tree.get_key(tree.nodes[0], '')
        data = tree.yeehaw()
        metadata.key = tree.key
        compressed_file = CompressedFile(metadata=dataclasses.asdict(metadata), data=data)
        compressed_file.write(filepath=metadata.output_path)

    def decompress(self, metadata):
        """Decompress function for Huffman's algorithm."""
        data = utils.read(metadata.input_path)
        compressed_file = CompressedFile(metadata=dataclasses.asdict(metadata), data=data)
        compressed_file.read(metadata=metadata)
        keys = compressed_file.metadata['key']
        data = compressed_file.data.decode('utf-8')
        # keys = self.get_keys_from_data(data)
        print(compressed_file.data)
        root = HuffmanTree(data).generate_tree_from_keys(keys)
        decompressed_data = self.get_data_from_tree(data, root)
        print(decompressed_data)
        print(compressed_file.output_path)
        utils.write(bytestream=str.encode(decompressed_data), filepath=compressed_file.output_path)
        return decompressed_data
        # utils.write(data, output_path)
    
    def get_keys_from_data(self, data):
        return ''

    def get_data_from_tree(self, data, root):
        decompressed_data = ''
        current_node = root
        for bit in data:
            if (bit == '0'):
                current_node = current_node.l_child
            elif (bit == '1'):
                current_node = current_node.r_child
            if (current_node.l_child == None and current_node.r_child == None):
                decompressed_data += current_node.characters
                current_node = root
        return decompressed_data

def traverse(rootnode):
  thislevel = [rootnode]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print (n.characters),
      if n.l_child: nextlevel.append(n.l_child)
      if n.r_child: nextlevel.append(n.r_child)
    print
    thislevel = nextlevel
