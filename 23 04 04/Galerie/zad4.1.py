file = open("galerie.txt", "r")
def parse_galleries(f):
  g = []
  for count,line in enumerate(f):
    arr = line.split()
    galeria = {
      'country': arr[0],
      'city': arr[1],
      'rooms': []
    }
    x = 0
    y = 0
    for i in range(2, len(arr), 2):
      if arr[i] == '0':
        break
      galeria['rooms'].append((int(arr[i]), int(arr[i+1])))
    g.append(galeria)
  return g
galerie = parse_galleries(file)
countries = {}
for i in galerie:
  if i['country'] in countries:
    countries[i['country']] += 1
  else:
    countries[i['country']] = 0
for count,country in enumerate(countries):
  print(country + " " + str(count))