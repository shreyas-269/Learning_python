class namaste():
    def greet(self, name): #Name is the parameter. Parameter is something that is about to be filled up with something. Its usually inside the paranthesis of a function.
        self.name = name #self.name is the attribute. Attribute is a variable that belongs to an object/a class. Its like the parameter of class, it gets the value from the parameter through an argument.
        print(f"Namaste {self.name}")
    
halo = namaste()
halo.greet("Izumi") #"Izumi" is the argument. It belongs to the object.

