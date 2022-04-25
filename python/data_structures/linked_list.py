from pickle import TRUE


class Node:
    # Creates node
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # Creates linked list

    def __init__(self):
        #  instantiate an empty linked list
        self.head = None

    def __str__(self):
        # returns a collection of all values within linked list
        string = ""
        current = self.head
        while current:
            string += f"{{ {current.value} }} -> "
            current = current.next
        return string + "NULL"


    def insert(self, value):
        # creates and inserts new node into linked list
        self.head = Node(value, self.head)

    def includes(self, target):
        # return true or false when finding a value within the linked list
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

class TargetError:
    pass
