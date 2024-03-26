class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(f'Punkt {x}:{y}')
    def ustaw(self,x,y):
        self.x = x
        self.y = y
    def __del__(self):
        print(f'Zwolniono pamięć dla {self.x}:{self.y}')

p = Punkt(2,3)
del p