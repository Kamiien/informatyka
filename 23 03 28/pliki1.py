file = open("dane.txt", "r")
wynik = open("wynik.txt", "w")
for count,line in enumerate(file):
  arr = line.split()
  arr = [int(i) for i in arr]
  arr.sort()
  wynik.write(str(arr[0]) + " " + str(arr[1]) + "\n")