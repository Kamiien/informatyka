class Item:
    value = 0
    weight = 0
    number = 0
    true_value = 0.0

    def __init__(self, value: int, weight: int, number = -1) -> None:
        self.value = value
        self.weight = weight
        self.number = number
        self.true_value = value / weight

    def __repr__(self) -> str:
        return 'Wartość: ' + str(self.value) + "; Waga: " + str(self.weight)

class Inv:
    capacity = 0
    used = 0
    free = 0
    items = []

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.free = capacity

    def add_item(self, item: Item):
        self.used += item.weight
        self.free -= item.weight
        items.append(item)

items = [
    Item(8,4),
    Item(1,2),
    Item(1,1),
    Item(3,2),
    Item(1,7)
]

inv = Inv(2000)

items.sort(key=lambda x: x.true_value, reverse=True)

print(items)
for x in range(len(items)):
    if items[x].weight < inv.free:
        inv.add_item(items[x])
        items[x].number -= 1
