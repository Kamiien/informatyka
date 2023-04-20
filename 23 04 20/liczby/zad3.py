file = open("liczby.txt", "r")
l = 0
for line in file:
  if len(line.strip('\n')) == 2:
    l += 1
print(l)