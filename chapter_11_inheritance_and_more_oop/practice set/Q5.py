class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def defining_vector(self):
        return f"{self.x}i + {self.y}j +{self.z}k"
    
    def __add__(self,other):
        return f"{self.x + other.x}i + {self.y + other.y}j + {self.z + other.z}"

    def __mul__(self,other):
        return f"{self.x * other.x}i + {self.y*other.y}j + {self.z*other.z}k"
    
v1 = vector(3,4,5)
v2 = vector(1,6,7)
print(v1 + v2)
print(v1*v2)
v3 = v1.defining_vector()
print(v3)

