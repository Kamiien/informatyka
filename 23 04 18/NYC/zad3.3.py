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
avg = 0
l = 0
for i in days:
  avg += i['temperature']
avg /= len(days)
for i in days:
  if i['temperature'] < avg:
    l += 1
print(l)