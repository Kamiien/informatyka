file = open('szachownice.txt', 'r')
szachownice = []
for i in file:
  i = i.strip('\n')
  szachownica = []
  for y in range(8):
    wiersz = []
    for x in range(8):
      wiersz.append(i[y * 8 + x])
    szachownica.append(wiersz)
  szachownice.append(szachownica)

l = 0
for sz in szachownice:
  for y in range(8):
    for x in range(8):
      if sz[y][x] == 'H':
        if y == 0 or y == 7 or x == 0 or x == 7:
          l += 1
print(l)