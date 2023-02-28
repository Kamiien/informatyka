def a(n):
  if n == 1:
    return 5
  elif n == 2:
    return -1
  else:
    return a(n-1) + 2 * a(n-2)

def aa(n):
  if n == 1:
    return 1.5
  if n == 2:
    return 0
  if n == 3:
    return -1.5
  return 3 * aa(n-1) + aa(n-2) - 2 * aa(n-3)

for x in range(15):
  print(a(x))