t = [3,3,8,7,4,4,3,3,3]
n = len(t)

kandydat = t[0]
p = 0

for i in range(n):
    if p == 0:
        kandydat = t[i]
        p = 1
    else:
        if t[i] == kandydat:
            p += 1
        else:
            p -= 1
if p == 0:
    print("brak lidera")
else:
    licznik = 0
    for i in range(n):
        if t[i] == kandydat:
            licznik += 1
    if licznik > n / 2:
        print("Lider = ", kandydat)
    else:
        print("Brak lidera")
