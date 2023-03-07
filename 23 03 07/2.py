#program sprawdzi i wypisze która wartość tablicy występuje najczęściej i ile razy
t = [2,4,5,5,5,6,6,7,2,6]
l = 0
lg = 1
n = 0
ng = 0
for i in range(1,len(t)):
  n = t[i]
  if t[i] == t[i-1]:
    l += 1
    if l > lg:
      lg = l
      ng = n
  else:
    l = 1

print("Długość = ", lg)
print("Liczba = ", ng)