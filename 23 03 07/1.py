#napisać program który wyznaczy w tablicy n elementowej długość najdłuższego podciągu stałego
t = [2,4,5,5,5,6,6,7,2,6]
max_g = 1
max = 1
poz_g = 0
poz = 0
for i in range(1,len(t)):
  if t[i] > t[i-1]:
    max += 1
    if max > max_g:
      max_g = max
      poz_g = poz
  else:
    max = 1
    poz = 1

print("Długość = ", max_g)
print("Pozycja = ", poz_g)