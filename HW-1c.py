start, end = map(open("in.txt").readlines()[:2])
  for num in range(start, end + 1):
    print(f"\nTable of {num}:")
    for i in range(1, 11):
      product = num * i
      print(f"{num} * {i} = {product}")

