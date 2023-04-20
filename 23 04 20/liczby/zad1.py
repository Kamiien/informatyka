def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

file = open("liczby.txt", "r")
l = 0
for line in file:
  if is_prime(int(line)):
    l += 1
print(l)