x = input()
l = 0
if len(x) < 5:
  print('Za krótkie')
  exit()
else:
  a = x[0]
  for i in range(0,len(x)):
    if x[i] == a:
      l += 1

if l == 5:
  print(a)
else:
  print('Błąd')
  exit()