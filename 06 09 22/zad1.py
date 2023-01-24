def oblicz(n):
  if n == 0:
    return 77
  if n == 1:
    return 50
  return oblicz(n-2) - oblicz(n-1) + 10
i = 0
while True:
  if oblicz(i) < 0:
    break
  i += 1
print('Wyraz numer ' + str(i) + ' jest pierwszą liczbą ujemną. Ma wartość ' + str(oblicz(i)))