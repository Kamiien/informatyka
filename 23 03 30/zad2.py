file = open("liczby.txt", "r")
l = 0
p = 0
for count,line in enumerate(file):
  n = int(line.strip("\n"))
  if p == n:
    l += 1
  p = n
print(l)