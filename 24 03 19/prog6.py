from dataclasses import dataclass

@dataclass
class A:
    x: int
    y: list[int]
@dataclass
class B:
    klasa: int
    n: A
