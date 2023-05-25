file = open("mecz.txt", "r")

mecze = [*file.readline().strip()]

a = 0
b = 0

for m in mecze:
    if m == "A":
        a += 1
    else:
        b += 1
    if a >= 1000 and a - b >= 3:
        print(f"Drużya A wygrała pierwszego seta {a} do {b}")
        break
    elif b >= 1000 and b - a >= 3:
        print(f"Drużyna B wygrała pierwszego seta {b} do {a}")
        break
