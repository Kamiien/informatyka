def silnia(n):
  if n == 0:
    return 1
  if n == 1:
    return 1
  return n * silnia(n-1)

file = open("liczby.txt", "r")
for count,line in enumerate(file):
  arr = [*line.strip("\n")]
  arr = [int(i) for i in arr]
  num = int(line.strip("\n"))
  fac = 0
  for i in arr:
    fac += silnia(i)
  if num == fac:
    print(num)