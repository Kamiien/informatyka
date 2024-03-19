from dataclasses import dataclass
import math

@dataclass
class Punkt:
    x: float
    y: float

@dataclass
class Prosta:
    a: float
    b: float
    c: float

punkt = Punkt(3, 4)
prosta = Prosta(-2, 1, 5)
odlegosc = abs(prosta.a * punkt.x + prosta.b * punkt.y + prosta.c) / math.sqrt(prosta.a**2 + prosta.b**2)
print(odlegosc)