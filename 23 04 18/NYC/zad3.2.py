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
l = 1
sg = days[0]['date']
eg = days[0]['date']
sl = days[0]['date']
el = days[0]['date']
for p,c in zip(days, days[1:]):
  if p['temperature'] > c['temperature']:
    if el - sl > eg - sg:
      eg = el
      sg = sl
    sl = c['date']
    el = c['date']
  if p['temperature'] <= c['temperature']:
    el = c['date']

print(str(sg) + ' ' + str(eg))
print(eg - sg + datetime.timedelta(1))