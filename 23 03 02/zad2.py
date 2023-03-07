def max(a,b):
    if a > b:
        return a
    else:
        return b

t = [2,3,4,1,3,5,8,6,9,2]
l = [1 for i in range(len(t))]
maxg = 1
for i in range(1,len(t)):
    maxl = 1
    for j in range(i):
        if t[j] < t[i]:
            maxl = max(l[j]+1,l[i])
    l[i] = maxl
    if maxl > maxg:
        maxg = maxl
for i in l:
    print(i)
