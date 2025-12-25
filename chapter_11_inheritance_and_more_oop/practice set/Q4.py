class complex:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        complex_number = f"{real_part} + {imaginary_part}i"

    def __add__(self, other):
        return f"{self.real_part + other.real_part} + {self.imaginary_part + other.imaginary_part}i"
    
    def __mul__(self, other):
        return f"{self.real_part*other.real_part + self.imaginary_part*other.imaginary_part} + {self.real_part*other.imaginary_part + self.imaginary_part*other.real_part}i"
    
c1 = complex(2,3)
c2 = complex(4,5)
c3 = c1 + c2
print(c3)
c4 = c1*c2
print(c4)

        
    
    
    