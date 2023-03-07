#napisać program który wyznaczy w tablicy n elementowej długość najdłuższego podciągu stałego
t = [2,4,5,5,5,6,6,7,2,6]
l = 0
lg = 1
for i in range(1,len(t)):
  if t[i] == t[i-1]:
    l += 1
    if l > lg:
      lg = l
  else:
    l = 1

print("Długość = ", lg)