from data_structures.kary_tree import KaryTree, Node
from data_structures.queue import Queue

def fizz_buzz_tree(tree):
    q = Queue()
    new_tree = KaryTree(Node(tree.root.value))
    print(new_tree.root.children)
    q.enqueue(new_tree.root)
    while not q.is_empty():
        front = q.dequeue()
        front.value = function(front.value)
        for i in front.children:
            q.enqueue(i)
    print(new_tree == tree)
    return new_tree


def function(num):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
