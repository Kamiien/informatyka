file = open("mecz.txt", "r")

mecze = [*file.readline().strip()]

l = 1
ldp = 0
ndp = 0
d = True  # True - A, False - B

for prev, curr in zip(mecze, mecze[1:]):
    if prev == curr:
        l += 1
    else:
        if l >= 10:
            ldp += 1
            if l >= ndp:
                d = True if prev == "A" else False
                ndp = l
        l = 1
print(f"Dobre passy: {ldp}")
print(
    f"Najdłuższa dobra passa osiągnięta przez drużynę {'A' if d else 'B'} o długości {ndp}"
)
