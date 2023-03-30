file = open("liczby.txt", "r")
p = 0
n = 0
for count,line in enumerate(file):
  n = int(line.strip("\n"))
  if n % 2 == 0:
    p += 1
  else:
    n += 1
print("Parzyste " + str(p))
print("Nieparzyste " + str(n))