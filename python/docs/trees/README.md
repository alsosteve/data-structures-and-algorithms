# [Data Structures and Algorithms](https://alsosteve.github.io/data-structures-and-algorithms/)
## [Language: Python](https://alsosteve.github.io/data-structures-and-algorithms/python/)

# Trees
## Feature Tasks
Challenge Type: New Implementation

### Node
* Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

### Binary Tree
* Create a Binary Tree class
  * Define a method for each of the depth first traversals:
    * pre order
    * in order
    * post order which returns an array of the values, ordered appropriately.
*Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

### Binary Search Tree
* Create a Binary Search Tree class
  * This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  * Add
    * Arguments: value
    * Return: nothing
    * Adds a new node with that value in the correct location in the binary search tree.
  * Contains
    * Argument: value
    * Returns: boolean indicating whether or not the value is in the tree at least once.

## Whiteboard Process
![challenge15](15.png)

## Examples
None

## Unit Tests
1. Can successfully instantiate an empty tree
2. Can successfully instantiate a tree with a single root node
3. For a Binary Search Tree, can successfully add a left child and right child properly to a node
4. Can successfully return a collection from a preorder traversal
5. Can successfully return a collection from an inorder traversal
6. Can successfully return a collection from a postorder traversal
7. Returns true  |  false for the `contains` method, given an existing or non-existing node value

## Stretch Goal
Create a new branch called `k-ary-tree`, and, using the resources available to you online, implement a k-ary tree, where each node can have any number of children.

## Approach & Efficiency
