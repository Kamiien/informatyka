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

avgs = []
for i in range(7):
  avg = {
  'value': 0,
  'count': 0
  }
  avgs.append(avg)
for i in days:
  avgs[i['date'].weekday()]['value'] += i['temperature']
  avgs[i['date'].weekday()]['count'] += 1
for i,v in enumerate(avgs):
  avgs[i]['value'] = v['value'] / v['count']
for i in avgs:
  print(str(i['value']))