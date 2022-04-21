def insert_shift(list, val):
  mid = len(list)-(len(list)//2)
  low = []
  high = []

  for i in list:
    if (list[i-1]) <= mid:
      low.append(list[i-1])
  else:
      high.append(list[i-1])

  return(low + [val] + high)
