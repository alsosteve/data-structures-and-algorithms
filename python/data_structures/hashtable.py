from data_structures.linked_list import LinkedList


class Hashtable:
    """
    Creates hashtable
    """

    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        #  Returns: Index in the collection for that key
        sum_of_chars = 0

        for char in key:
            sum_of_chars += ord(char)

        primed = sum_of_chars * 599

        index = primed % self.size

        return index

    def set(self, key, value):
        # hash the key, and set the key and value pair in the table
        index = self.hash(key)

        bucket = self.buckets[index]

        if bucket is None:
            bucket = LinkedList()
            self.buckets[index] = bucket

        # TODO: handle updates vs adds - Test for it!
        bucket.insert((key, value))

    def get(self, key):
        # Returns: Value associated with that key
        index = self.hash(key)
        bucket = self.buckets[index]

        current = bucket.head

        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]

            current = current.next

        return None

    def contains(self, key):
        # Returns: Boolean, indicating if the key exists in the table
        index = self.hash(key)
        bucket = self._buckets[index]

        if bucket is None:
            return False

        current = bucket.head

        while current:
            if current.value[0] == key:
                return True
            current = current.next
        return False
