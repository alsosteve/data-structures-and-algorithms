def binary_search(list, n, low, high):
  if high >= low:
    mid = (high + low) // 2
    if list[mid] == n:
            return(mid)
    elif list[mid] > n:
            return binary_search(list, n, low, mid - 1)
    else:
      return binary_search(list, n, mid + 1, high)

  else:
    return(-1)