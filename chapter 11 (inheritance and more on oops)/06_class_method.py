class employee():
    a = 1
    def show(self):
        print(f"The class value of a is {self.a}")
    
b = employee()
b.a = 45
b.show()

#But we want it to show the class value of a that is 1 as stated in the print command.
class employee2():
    c = 1
    @classmethod #Decorator of class method.
    def show2(cls): #cls denotes the class that contains the object on which the method is being used.
        print(f"The class value of a is {cls.c}") #cls.a means attribute of the class.
    
d= employee2()
d.c = 45
d.show2()