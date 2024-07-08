def print_tables(start, end):
  for num in range(start, end + 1):
    print(f"\nTable of {num}:")
    for i in range(1, 11):
      product = num * i
      print(f"{num} * {i} = {product}")

try:
  start = int(input("Enter starting number (positive integer): "))
  end = int(input("Enter ending number (greater than or equal to starting number): "))
  if start < 0 or end < start:
    print("Invalid input. Please enter positive integers with ending number greater than or equal to starting number.")
  else:
    print_tables(start, end)
