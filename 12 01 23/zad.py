def f(a, b, h):
  return (a + b) * h / 2

n = 20
p = -5
q = 5
d = (abs(p) + abs(q)) / n
pole = 0

for i in range(0, n):
  pole += f(abs((p+i)**2), abs((p+i+1)**2), d)

print(pole)