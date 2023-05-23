file = open("liczby.txt", "r")

length = 0
median = 0
for l in file:
    median += int(l)
    length += 1
median /= length
print(median)
