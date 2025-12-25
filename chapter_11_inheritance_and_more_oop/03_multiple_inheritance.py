#When child inherits from more than 1 parent class.

#Parent class
class employee():
    company = "Rajesh paan waala"

    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of the employee is {self.name}\nThe salary of the employee is {self.salary}")

#2nd parent class
class coder():
    lang = "python"
    def print_lang(self):
        print(f"Your lang is {self.lang}")

#Child class
class programmer2(employee, coder): #Inherited class.
    company = "Rajesh Paan waala Khan Market"

    #Non inherited function.
    def show_language(self):
        print(f"The name of the employee is {self.name}\nThe language that person is good in is {self.language}")

c = employee()
d = programmer2()
print(c.company, d.company)
d.show("Izumi", "1rs")
d.print_lang()