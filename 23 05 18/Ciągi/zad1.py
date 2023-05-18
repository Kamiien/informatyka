ciagi = []
file = open("ciagi.txt", "r")
for x in file:
    ciag = x.split()
    if len(ciag) <= 1:
        continue
    ciag = [int(i) for i in ciag]
    ciagi.append(ciag)
print(ciagi)

gf = 0
lf = 0
gl = 0
ll = 0
arr = []
for x in ciagi:
    for prev, curr in zip(x, x[1:]):
        if curr > prev:
            ll += 1
        else:
            lf += 1
        if ll < lf:
            ll = lf
    if ll - lf > gl - gf:
        gl = ll
        gf = lf
        arr = x[(gf) : (gl + 1)]
    lf = 0
    ll = 0
print(f"{gf} {gl}")
print(arr)
