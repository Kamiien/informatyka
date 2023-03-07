s = input("Podaj wyraz do zaszyfrowania: ")
h = int(input("Podaj wysokość płotu: "))
plot = [['' for x in range(len(s))] for y in range(h)]

l = 0
kierunek = True

for i in range(len(s)):
  plot[l][i] = s[i]
  if kierunek:
    l += 1
  else:
    l -= 1
  if l == 0:
    kierunek = True
  if l == h-1:
    kierunek = False

szyfrogram = ""

for x in range(h):
  for y in range(len(s)):
    if plot[x][y] != '':
      szyfrogram += plot[x][y]

print(szyfrogram)