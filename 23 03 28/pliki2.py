file = open("dane2.txt", "r")
wynik = open("wynik2.txt", "w")
max = 0
for count,line in enumerate(file):
  arr = line.split()
  arr = [int(i) for i in arr]
  arr.sort()
  wynik.write(str(arr[2]) + "\n")
  if arr[2] > max:
    max = arr[2]

print(max)