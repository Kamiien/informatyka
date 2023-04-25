def does_attack(x1,y1,x2,y2):
  if x1 == x2 and y1 == y2:
    return False
  if y1 == y2:
    return True
  if x1 == x2:
    return True
  for i in range(7):
    if (y1-(i+1)) == y2 and (x1-(i+1)) == x2:
      return True
  for i in range(7):
    if (y1+(i+1)) == y2 and (x1-(i+1)) == x2:
      return True
  for i in range(7):
    if (y1-(i+1)) == y2 and (x1+(i+1)) == x2:
      return True
  for i in range(7):
    if (y1+(i+1)) == y2 and (x1+(i+1)) == x2:
      return True
  return False


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
      if sz[y][x] == 'H' and does_attack(x,y,4,2):
        l += 1
print(l)