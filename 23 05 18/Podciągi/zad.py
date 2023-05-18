file = open("ciagi.txt", "r")
ciagi = []
for x in file:
    ciag = x.split()
    if len(ciag) <= 1:
        continue
    ciag = [int(i) for i in ciag]
    ciag.pop(0)
    ciagi.append(ciag)
print(ciagi)

g = 0
gi = 0
for i, x in enumerate(ciagi):
    l = 0
    for prev, curr in zip(x, x[1:]):
        if curr > prev:
            l += 1
        else:
            if l > g:
                g = l
                gi = i - 1
            l = 1
    if l > g:
        g = l
        gi = i
print(gi)

g = 0
gi = 0
for i, x in enumerate(ciagi):
    l = 0
    for prev, curr in zip(x, x[1:]):
        if curr == prev:
            l += 1
        else:
            if l > g:
                g = l
                gi = i - 1
            l = 0
    if l > g:
        g = l
        gi = i
print(gi)
