"""Tests for third problem"""
import pytest
from node import Node
from solution import serialize_tree, deserialize_tree

@pytest.mark.parametrize(
    "root, value",
    [
        (Node('root', Node('left', Node('left.left')), Node('right')), 'left.left'),
        (Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6))), '4'),
        (Node('A', Node('B', Node('C'), Node('D')), Node('E', Node('F'), Node('G'))), 'C'),
        (Node(0, Node(1, Node(3), Node(4)), Node(2)), '3'),
        (Node('root', Node('left', Node('deep.left')), Node('right')), 'deep.left'),
        (Node(10, Node(20, Node(30, Node(40), Node(50)), Node(60)), Node(70)), '30'),
        (Node('X', Node('Y', Node('Z'))), 'Z'),
        (Node(100, Node(50, Node(25)), Node(150, Node(125), Node(175))), '25'),
        (Node('center', Node('left', Node('inner.left')), Node('right')), 'inner.left'),
    ],
)
def test_should_return_left_left_value(
        root: Node, value: str
    ) -> None:
    """
    Test serialization and deserialization
    of Binary Tree nodes: left side
    """
    assert deserialize_tree(serialize_tree(root)).left.left.val == value

@pytest.mark.parametrize(
    "root, value",
    [
        (Node('root', Node('left', Node('left.left')), Node('right')), 'right'),
        (Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6))), '3'),
        (Node('A', Node('B', Node('C'), Node('D')), Node('E', Node('F'), Node('G'))), 'E'),
        (Node(10, Node(5), Node(15)), '15'),
        (Node('start', Node('left', Node('left.left')), Node('right')), 'right'),
        (Node('root', Node('left'), Node('right', Node('deep.right'))), 'right'),
        (Node('X', Node('Y', Node('Z')), Node('W')), 'W'),
        (Node(20, Node(10), Node(30)), '30'),
        (Node('center', Node('left'), Node('right', Node('inner.right'))), 'right'),
        (Node(100, Node(50), Node(150, Node(125), Node(175))), '150'),
    ],
)
def test_should_return_right_value(
        root: Node, value: str
    ) -> None:
    """
    Test serialization and deserialization
    of Binary Tree nodes: left side
    """
    assert deserialize_tree(serialize_tree(root)).right.val == value

@pytest.mark.parametrize(
    "root",
    [
        (Node('root', Node('left', Node('left.left')), Node('right'))),
        (Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6))))
    ],
)
def test_should_return_none_leaf(
        root: Node
    ) -> None:
    """
    Test serialization and deserialization
    of Binary Tree nodes: leaf should be None
    """
    assert deserialize_tree(serialize_tree(root)).left.left.left is None
