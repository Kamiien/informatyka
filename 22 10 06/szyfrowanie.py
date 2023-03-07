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

szyfrogram = ''
l = 0

for x in range(len(z)):
  if z[x] == ' ':
    szyfrogram += ' '
  else:
    szyfrogram += szyfrowe[l % len(szyfrowe)][jawny.index(z[x])]
    l += 1

print(szyfrogram)