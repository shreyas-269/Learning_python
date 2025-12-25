class twoD:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def display(self):
        print(f"{self.x}i + {self.y}j")

class threeD(twoD):
    def __init__(self, x=0, y=0, z=0):
        self.z = z
        super().__init__(x, y)
    def display(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")

v2 = twoD(3, 4)
v2.display()

v3 = threeD(2, 5, 7)
v3.display()