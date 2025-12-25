#A function that doesnt use the self parameter.
#It doesnt need access to the object/instance (self is the object in this case).
#It behaves like a normal function but its grouped logically inside a class.
#It is defined by @staticmethod decorator.
#A decorator in python is a special function that modifies another function without changing its code. It starts with a @ symbol.


class employee:
    lang = "python"
    salary = "1rs"

    def greet(self): #This function is just printing good morning. But we passed an whole object for it.
        print(f"Good morning {self.name}") 
    
    @staticmethod
    def greet_in_the_evening(name):
        print(f"Good evening {name}")

    
izumi = employee() #This variable is the object.
izumi.name = "Izumi" #This literally means that the name of the object izumi is Izumi
print(izumi.name, izumi.lang, izumi.salary)
izumi.greet()
izumi.greet_in_the_evening(izumi.name)


kyouko = employee()
kyouko.name = "Kyouko"
print(kyouko.name, kyouko.lang, kyouko.salary)
kyouko.greet()
kyouko.greet_in_the_evening(kyouko.name)

