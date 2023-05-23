def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


file = open("dane.txt", "r")

dane = []
for l in file:
    arr = l.split()
    dane.append((int(arr[0]), int(arr[1])))

gnwd = 0
print("NWD:")
for d in dane:
    n = nwd(d[0], d[1])
    if n > gnwd:
        gnwd = n
    print(f"A: {d[0]} B: {d[1]} NWD: {n}")
print(f"Największe NWD: {gnwd}")

gpn = 0
for x in dane:
    for y in x:
        if is_prime(y) and y > gpn:
            gpn = y
print(f"Największa liczba pierwsza: {gpn}")
