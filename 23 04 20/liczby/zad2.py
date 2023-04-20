file = open("liczby.txt", "r")
liczby = []
for line in file:
  liczby.append(int(line))

len = 1
max = 1
for p,c in zip(liczby, liczby[1:]):
  if p > c:
    len += 1
  else:
    if len > max:
      max = len
    len = 1
print(max)