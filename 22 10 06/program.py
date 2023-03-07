print('1. Szyfrowanie')
print('2. Odszyfrowanie')
print('3. Wyjście')
mode = int(input('Wybierz: '))
if mode == 3:
  exit()

z = input('Podaj zdanie lub wyraz: ').lower()
k = input('Podaj klucz: ').lower()
k = k.replace(' ', '')
k = ''.join(dict.fromkeys(k))
print(k)
jawny = 'abcdefghijklmnopqrstuvwxyz'
szyfrowe = [[*jawny] for x in range(len(k))]

for x in range(len(szyfrowe)):
  for y in range(jawny.index(k[x])):
    temp = szyfrowe[x][0]
    szyfrowe[x].pop(0)
    szyfrowe[x].append(temp)

s = ''
l = 0

if mode == 1:
  for x in range(len(z)):
    if z[x] == ' ':
      s += ' '
    else:
      s += szyfrowe[l % len(szyfrowe)][jawny.index(z[x])]
      l += 1
else:
  for x in range(len(z)):
    if z[x] == ' ':
      s += ' '
    else:
      s += jawny[szyfrowe[l % len(szyfrowe)].index(z[x])]
      l += 1

print(s)