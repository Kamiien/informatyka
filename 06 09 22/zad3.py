x = input()
l_0 = 0
l_1 = 0
if len(x) != 5:
  print('Nie jest długości 5')
  exit()
else:
  for i in range(0, len(x)):
    if x[i] == '0':
      l_0 += 1
    if x[i] == '1':
      l_1 += 1
if l_0 > l_1:
  print('0')
else:
  print('1')