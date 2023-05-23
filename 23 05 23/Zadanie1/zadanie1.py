file = open("miejsca.txt", "r")


def parse(f):
    cities = []
    for count, line in enumerate(f):
        arr = line.split()
        if len(arr) < 4:
            continue
        city = {"Country": arr[0], "City": arr[1], "X": int(arr[2]), "Y": int(arr[3])}
        cities.append(city)
    return cities


cities = parse(file)
for c in cities:
    if c["X"] * c["Y"] > 1000:
        print(c["City"])
