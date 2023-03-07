s = input("Podaj wyraz do odszyfrowania: ")
h = int(input("Podaj wysokość płotu: "))
plot = [['' for x in range(len(s))] for y in range(h)]

l = 0
kierunek = True

for i in range(len(s)):
  plot[l][i] = 0
  if kierunek:
    l += 1
  else:
    l -= 1
  if l == 0:
    kierunek = True
  if l == h-1:
    kierunek = False

l = 0

for x in range(h):
  for y in range(len(s)):
    if plot[x][y] == 0:
      plot[x][y] = s[l]
      l += 1

wyraz = ""

l = 0
kierunek = True

for i in range(len(s)):
  wyraz += plot[l][i]
  if kierunek:
    l += 1
  else:
    l -= 1
  if l == 0:
    kierunek = True
  if l == h-1:
    kierunek = False

print(wyraz)