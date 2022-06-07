from data_structures.binary_tree import BinaryTree


def tree_intersection(one, two):
    list = []
    common = []
    i = 0
    for node in one.in_order():
        list.append(node)
    print(list)

    for node in two.in_order():
        if list[i] == node:
            common.append(node)
        i+=1

    return common
