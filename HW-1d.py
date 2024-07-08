open("in.txt"), open("out.txt"):
  start, end = map(int, readline().strip().split(","))
  for num in range(start, end + 1):
    f_out.write(f"\nTable of {num}:\n")
    for i in range(1, 11):
      f_out.write(f"{num} * {i} = {num * i}\n")

print("Multiplication tables written to 'out.txt'.")
