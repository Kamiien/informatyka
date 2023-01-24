szyfrogram = input('Podaj zdanie lub wyraz: ').lower()
k = input('Podaj klucz: ').lower()
k = k.replace(' ', '')
k = ''.join(dict.fromkeys(k))
jawny = 'abcdefghijklmnopqrstuvwxyz'
szyfrowe = [[*jawny] for x in range(len(k))]

for x in range(len(szyfrowe)):
  for y in range(jawny.index(k[x])):
    temp = szyfrowe[x][0]
    szyfrowe[x].pop(0)
    szyfrowe[x].append(temp)

z = ''
l = 0

for x in range(len(szyfrogram)):
  if szyfrogram[x] == ' ':
    z += ' '
  else:
    z += jawny[szyfrowe[l % len(szyfrowe)].index(szyfrogram[x])]
    l += 1

print(z)