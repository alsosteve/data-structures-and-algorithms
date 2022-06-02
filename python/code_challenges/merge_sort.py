def merge_sort(list):
    n = len(list)
    if n > 1:
        mid = n//2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, list)
    return list

def merge(left, right, list):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
