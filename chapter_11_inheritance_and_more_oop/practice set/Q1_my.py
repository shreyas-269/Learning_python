class twoD:
    def abscissa(self, x):
        self.x = x
        return f"{x}"
    
    def ordinate(self, y):
        self.y = y
        return f"{y}"
    
class threeD(twoD):
    def z_coordinate(self, z):
        self.z = z
        return f"{z}"

class printing_the_vector:
    def twoD_vector(self):
        a = twoD()
        abscissa = a.abscissa(input("Enter the abscissa of 2D vector: "))
        ordinate = a.ordinate(input("Enter the ordinate of 2D vector: "))
        print(f"{abscissa}i + {ordinate}j")
    def threeD_vector(self):
        b = threeD()
        abscissa = b.abscissa(input("Enter the abscissa of 3D vector: "))
        ordinate = b.ordinate(input("Enter the ordinate of 3D vector: "))
        z_coordinate = b.z_coordinate(input("Enter the z coordinate of 3D vector: "))
        print(f"{abscissa}i + {ordinate}j + {z_coordinate}k")

twoD_v1 = printing_the_vector()
twoD_v1.twoD_vector()
threeD_v1 = printing_the_vector()
threeD_v1.threeD_vector()


            
    
