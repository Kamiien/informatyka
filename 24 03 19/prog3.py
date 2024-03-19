from dataclasses import dataclass
import math

@dataclass
class Punkt:
    x: int
    y: int

p1 = Punkt(0,0)
p2 = Punkt(6,3)
x1 = abs(p2.x - p1.x)
y1 = abs(p2.y - p1.y)
odleglosc = math.sqrt(x1**2 + y1**2)
print(odleglosc)