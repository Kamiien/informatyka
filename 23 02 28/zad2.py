def a(n):
  if n == 1:
    return 4
  return a(n-1) + 3

def b(n):
  if n == 1:
    return 5
  return b(n-1) / 2

def c(n):
  if n == 1:
    return 2
  return c(n-1) * -1

def d(n):
  if n == 1:
    return 4
  if n == 2:
    return 6
  return d(n-2) + 1

def e(n):
  if n == 1:
    return 0
  if n == 2:
    return 1
  if n == 3:
    return -1
  if n % 2 == 0:
    return e(n-2) + 1
  else:
    return e(n-2) - 1