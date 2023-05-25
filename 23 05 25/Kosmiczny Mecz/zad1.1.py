file = open("mecz.txt", "r")

mecze = [*file.readline().strip()]

l = 0
for prev, curr in zip(mecze, mecze[1:]):
    if prev != curr:
        l += 1
print(l)
