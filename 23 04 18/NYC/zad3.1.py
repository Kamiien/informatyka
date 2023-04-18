import datetime

file = open("temperatury_nowy_york.txt", "r")
def fill(f):
  days = []
  for count,line in enumerate(f):
    arr = line.split()
    date = arr[0].split('.')
    day = {
      'date': datetime.date(int(date[2]), int(date[1]), int(date[0])),
      'temperature': int(arr[1]),
    }
    days.append(day)
  return days
days = fill(file)
g = 1
l = 1
o = 0
for p,c in zip(days, days[1:]):
  if p['temperature'] == c['temperature']:
    l += 1
  else:
    if l > g:
      g = l
    if l > 1:
      l = 1
      o += 1
print(g)
print(o)