integer = 1
print(type(integer)) #The output is class int. Everything in python is class.

#Operator overloading makes your custom objects work like built in operators.
#This is done by dunder methods inside the class.
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# p1 = point(1,3)
# p2 = point(2,4)
# p3 = p1 + p2
# print(p3)
#This will give an error.
#Because the coordinates of the point in the class are self defined, not built in. Operator overloading converts those custom objects into built in.

    def __add__(self, other): #__add__ is a dunder method which creates a built in operator out of custom objects. Self is the point on the left and other is the point on the right.
        return point(self.x + other.x, self.y + other.y) #This point() will create a point out of it.
    
    def __sub__(self, other):
        return point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return "Both the points are equal."
        else:
            return "Both the points are not equal."
        
    
#Now the above code will work.
p1 = point(1,3)
p2 = point(2,4)
p3 = p1 + p2
print(p3.x, ",", p3.y)
p4 = p1 - p2
print(p4.x, ",", p4.y)
p5 = point(1,3)
print(p1 == p5)

class student:
    def __init__(self, name, student_class):
        self.name = name
        self.student_class = student_class
    def __str__(self):
        return f"Name:{self.name}\nclass:{self.student_class}"

s1 = student("Izumi", "12th")
print(s1)
    






