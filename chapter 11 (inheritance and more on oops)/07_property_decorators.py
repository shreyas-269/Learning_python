class employee2():
    c = 1
    
    @classmethod #Decorator of class method.
    def show2(cls): #cls denotes the class that contains the object on which the method is being used.
        print(f"The class value of a is {cls.c}") #cls.a means attribute of the class.
    
    @property #A property decorator lets you use methods like attributes.
    #It gives you control over getting, setting and deleting values.
    def name(self): #This method name is also an attribute now. It gets value from a parameter through an argument.
        return f"{self.fname} {self.lname}" #This return value can be used by the coder as an attribute in other functions, the name of the attribute will be 'value' only.
    
    @name.setter #Setter attribute is a part of property attribute. Name is an attribute cause of the property decorator. name.setter means setting the value of name. The value is put inside the function inside the setter decorator.
    def name(self,value): #Here the value is the value returned by the function name. Value is the arguement passed to the setter.
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1] 
        #Split function splits the string "Izumi Miyamura" into a list ["Izumi", "Miyamura"] dividing the string before and after the whitespace.
        #fname(first name) is the string at the 0th index of the list.
        #lname(last name) is the string at the 1st index of the list.
#This code is used when we dont want the user to enter their first and last name separately cause they might be uncomfortable.
#It asks the user to enter their name and then divides it by itself.

d= employee2()
d.c = 45
d.show2()
d.name = "Izumi Miyamura"
print(d.name)

#This is abstraction and encapsulation.
#Abstraction is the process of hiding complex implementation details.
#It shows only the essential features of an object.
#Its goal is to simplify the system for the user.
#Encapsulation hides the data(in this case attributes).
#It bundles the data (attributes) and methods that operate on that data (functions inside that class) into a single unit(class).
#This protects the data from the user.
#For example you can only change the bank balance by withdrawing or depositing money.



