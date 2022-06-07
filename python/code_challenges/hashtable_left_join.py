from data_structures.hashtable import Hashtable



def left_join(a, b):
    # joins two hashmaps into a single data structure
    output = []

    for key in a:
        join_left = [key, a.get(key), b.get(key)or "NONE"]
        output.append(join_left)

    # return output
    return output
