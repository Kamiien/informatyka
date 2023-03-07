s = input("Podaj string: ")
h1 = s[0:int(len(s)/2)]
h2 = s[int(len(s)/2):len(s)]
sz = h2 + h1
print(sz)