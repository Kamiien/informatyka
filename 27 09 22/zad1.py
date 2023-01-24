jawny = "abcdefghijklmnopqrstuvwxyz"
szyfrowy = []
print('1. Szyfrowanie')
print('2. Odszyfrowanie')
print('3. Wyjście')
tryb = int(input())
if tryb == 3:
  exit()
x = input('Podaj wyraz: ').lower()
k = input('Podaj klucz: ').lower()
k = k.replace(' ', '')
for i in k:
  if len(szyfrowy) == 26:
    break
  if szyfrowy.count(i) == 0:
    szyfrowy.append(i)

if len(szyfrowy) < 26:
  for i in jawny:
    if len(szyfrowy) == 26:
      break
    if(szyfrowy.count(i)) == 0:
      szyfrowy.append(i)

szyfrogram = []
if tryb == 1:
  for i in x:
    if i == ' ':
      szyfrogram.append(' ')
    else:
      szyfrogram.append(szyfrowy[jawny.index(i)])
else:
  for i in x:
    if i == ' ':
      szyfrogram.append(' ')
    else:
      szyfrogram.append(jawny[szyfrowy.index(i)])

print("".join(szyfrogram))