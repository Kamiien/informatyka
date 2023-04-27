import json

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
oceny = {}
for s in sluchacze:
  if not s['nazwa'] in oceny:
    oceny.update({s['nazwa']: []})
  srednia = 0
  if len(s['oceny']) > 0:
    x = 0
    l = 0
    for i in s['oceny']:
      l += 1
      x += i
    srednia = round(x / l)
  przedmiot = {
    "przedmiot": s['przedmiot'],
    "srednia": srednia
  }
  oceny[s['nazwa']].append(przedmiot)
print(json.dumps(oceny, indent=4))