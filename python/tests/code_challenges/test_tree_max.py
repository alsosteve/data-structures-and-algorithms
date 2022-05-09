import pytest
from data_structures.binary_tree import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_another_max_val():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    actual = tree.find_maximum_value()
    expected = 7

    assert actual == expected

# @pytest.mark.skip("TODO")
def test_empty_tree():
    tree = BinaryTree()

    actual = tree.find_maximum_value()
    expected = None

    assert actual == expected
