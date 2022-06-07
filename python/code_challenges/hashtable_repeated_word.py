from data_structures.hashtable import Hashtable
from data_structures.linked_list import LinkedList
import re

def first_repeated_word(str):
    str = str.lower()
    table = Hashtable()
    str = re.sub(r'[^\w\s]','', str) # remove Punctuation
    word_list = str.split()

    for word in word_list:
    # hash the key, and set the key and value pair in the table
        index = table.hash(word)
        bucket = table.buckets[index]

        # first instance
        if bucket is None:
            bucket = LinkedList()
            table.buckets[index] = bucket
        # second instance
        else: return word

        bucket.insert((word, 1))

