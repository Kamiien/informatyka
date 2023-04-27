file = open('oceny.txt', 'r')
def fill(f):
  sluchacze = []
  for count,line in enumerate(f):
    arr = line.split()
    oceny = []
    if len(arr) > 2:
      for i in range(2, len(arr)):
        oceny.append(int(arr[i]))
    sluchacz = {
      'nazwa': arr[0],
      'przedmiot': arr[1],
      'oceny': oceny
    }
    sluchacze.append(sluchacz)
  return sluchacze

sluchacze = fill(file)
nazwy = []
for s in sluchacze:
  if not s['nazwa'] in nazwy:
    nazwy.append(s['nazwa'])
print(len(nazwy))