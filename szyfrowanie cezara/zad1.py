jawny = "abcdefghijklmnopqrstuvwxyz"
szyfrowy = "abcdefghijklmnopqrstuvwxyz"
szyfrowy = [*szyfrowy]

x = input('Podaj zdanie: ')
k = int(input('Podaj kod: '))

for i in range(k):
  temp = szyfrowy[0]
  szyfrowy.pop(0)
  szyfrowy.append(temp)

szyfrogram = []
for i in range(len(x)):
  szyfrogram.append(szyfrowy[jawny.index(x[i])])

print([*jawny])
print(szyfrowy)
print("Szyfrogram: " + "".join(szyfrogram))