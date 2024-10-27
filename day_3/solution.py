"""
Solution for day 3 task
"""
from node import Node
LEAF = 'None'

def serialize_tree(root: Node) -> str:
    """
    Given the root to a binary tree, implement
    serialize(root), which serializes the tree 
    into a string.
    """
    if root is None:
        return LEAF
    return f'{root.val} {serialize_tree(root.left)} {serialize_tree(root.right)}'

def deserialize_tree(text: str) -> Node:
    """
    Given the root to a binary tree, implement
    deserialize(s), which deserializes the string 
    back into the tree.
    """
    def create_node():
        current = next(values)
        if current == LEAF:
            return None
        node = Node(current, create_node(), create_node())
        return node
    values = iter(text.split())
    return create_node()
