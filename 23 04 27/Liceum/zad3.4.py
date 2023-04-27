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
przedmioty = {}
for s in sluchacze:
  if not s['przedmiot'] in przedmioty:
    przedmioty.update({s['przedmiot']: 0})
for s in sluchacze:
  przedmioty[s['przedmiot']] += 1
pretty = json.dumps(dict(sorted(przedmioty.items(), key=lambda item: item[1], reverse=True)), indent=4)
print(pretty)