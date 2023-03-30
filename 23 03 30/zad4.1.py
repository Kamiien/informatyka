file = open("liczby.txt", "r")
potegi = [1]
while True:
  if 3 ** len(potegi) > 100000:
    break
  potegi.append(3 ** len(potegi))
print(potegi)
l = 0
for count,line in enumerate(file):
  n = int(line.strip("\n"))
  for i in potegi:
    if n == i:
      l += 1
print(l)