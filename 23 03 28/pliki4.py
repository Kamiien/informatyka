file = open("dane4.txt", "r")
arr = []
for count,line in enumerate(file):
  arr.append(int(line.strip("\n")))
  arr.sort()
avg = sum(arr) / len(arr)
for x in arr:
  if x > avg:
    print(x)