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

valid_pos = []
for x in range(8):
    valid_pos.append((x,x))
for y in range(8):
  for x in range(7, -1, -1):
    if x + y == 7:
      valid_pos.append((x,y))

hetman_pos = []
for sz in szachownice:
  for y in range(8):
    for x in range(8):
      if sz[y][x] == 'H':
        hetman_pos.append((x,y))

l = 0
for h in hetman_pos:
  for v in valid_pos:
    if h == v:
      l += 1
print(l)