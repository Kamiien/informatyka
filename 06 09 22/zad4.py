x = input()
l_0 = 0
l_1 = 0
licznik = 0
if len(x) % 5 != 0:
  print('Długość niepodzielna przez 5')
  exit()
else:
  for i in range(0, len(x)):
    if x[i] == '1':
      l_1 += 1
    else:
      l_0 += 1
    licznik += 1
    if licznik == 5:
      if l_1 > l_0:
        print('1', end='')
      else:
        print('0', end='')
      licznik = 0
      l_0 = 0
      l_1 = 0