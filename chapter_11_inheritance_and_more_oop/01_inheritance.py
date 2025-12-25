#Inheritance is a way of creating new class from existing class.

#Parent class
class employee():
    company = "Rajesh paan waala"

    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of the employee is {self.name}\nThe salary of the employee is {self.salary}")

#Class made using copy paste
class programmer():
    company = "Rajesh paan waala Hauz Khas"

    def show(self):
        print(f"The name of the employee is {self.name}\nThe salary of the employee is {self.salary}")

    def show_language(self):
        print(f"The name of the employee is {self.name}\nThe language that person is good in is {self.language}")

a = employee()
b = programmer()
print(a.company)
print(b.company)

#The function show() from employee was copied from employee() to programmer().
#What if there were 50 such classes that it had to be pasted into and it suddenly required a change in all 50 of them.
#That would be troublesome and prone to error with copy pasting.
#This is where inheritance is used.
#Syntax is child_class(parent_class).

#Child class
class programmer2(employee): #Inherited class.
    company = "Rajesh Paan waala Khan Market"

    #Non inherited function.
    def show_language(self):
        print(f"The name of the employee is {self.name}\nThe language that person is good in is {self.language}")

c = employee()
d = programmer2()
print(c.company, d.company)
d.show("Izumi", "1rs")

