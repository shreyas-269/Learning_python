class employee:
    lang = "python"
    salary = "1rs"

    def __init__(self):
        print("I am creating an object")
    
    def __init__(self, name, salary, lang):
        self.name = name
        self.salary = salary
        self.lang = lang
    #Now this function has been defined which automatically runs with employee() class. You give attributes inside the employee() paranthesis.
    #You have to give attributes whenever you create an object now.

    def greet(self):
        print("good morning")

izumi = employee("izumi", "1rs", "python")
print([izumi.name, izumi.salary,izumi.lang])

izumi.greet()

#__init__ function wasnt even called, still the output will have that printed.
#__init__ is a special method which is called dunder method in python. Its automatically called.
#dunder methods start with double underscore.

kyouko = employee("Kyouko", "2rs", "Java")
print([kyouko.name, kyouko.salary,kyouko.lang])

