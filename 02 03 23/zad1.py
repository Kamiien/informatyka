t = [2,3,4,1,3,5,2,6,9,2]
max_d = 1
max = 1
poz = 0
poz_global = 0
for i in range(1,len(t)):
  if t[i] > t[i-1]:
    max += 1
    if max > max_d:
      max_d = max
      poz_global = poz
  else:
    max = 1
    poz = 1

print("Długość = ", max_d)
print("Pozycja = ", poz_global)