wyraz = input('Podaj wyraz do zaszyfrowania: ')
wyraz = "".join(wyraz.split())
k = [*input('Podaj klucz: ')]
k = list(map(int,k))

dw = len(wyraz)
dk = len(k)
w = 0

if dw % dk == 0:
  w = dw // dk
else:
  w = dw // dk + 1
znaki = [['' for x in range(dk)] for x in range(w)]

l = 0
for i in range(w):
  for j in range(dk):
    if l < dw:
      znaki[i][j] = wyraz[l]
    l+=1

szyfrogram = ''
for i in range(dk):
  for j in range(w):
    szyfrogram += znaki[j][k[i]]

print(szyfrogram)