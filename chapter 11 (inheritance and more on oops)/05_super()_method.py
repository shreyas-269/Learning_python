# import random
# #Parent--> child 1 --> child 2.

# #Parent class
# class employee():
#     def __init__(self):
#         print("Constructor of employee")

#     company = "Rajesh paan waala"

#     def show(self, name, salary):
#         self.name = name
#         self.salary = salary
#         print(f"The name of the employee is {self.name}\nThe salary of the employee is {self.salary}")

# #Child1 class
# class programmer(employee): #Inherited class.
#     def __init__(self):
#         print("Constructor of programmer")

#     company = "Rajesh Paan waala Khan Market"

#     #Non inherited function.
#     def show_language(self):
#         print(f"The name of the employee is {self.name}")

# #Child2 class
# class programmer_manager(programmer):
#     def __init__(self):
#         print("Constructor of programmer_manager.")

#     number_of_employees_under_him = random.randint(1,100)
    
#     def show_the_number_of_employees_under_him(self):
#         print(f"Number of employees under him are {self.number_of_employees_under_him}")

# izumi = programmer_manager()
# print(izumi.company)
# izumi.show("kyouko", "1rs")
# izumi.show_language()
# izumi.show_the_number_of_employees_under_him()

#The output of code uptill now will only give the constructor output of programmer_manager class.
#We want the parent constructor to work along with the child constructor in super() method.

import random
#Parent--> child 1 --> child 2.

#Parent class
class employee():
    def __init__(self):
        print("Constructor of employee")

    company = "Rajesh paan waala"

    def show(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of the employee is {self.name}\nThe salary of the employee is {self.salary}")

#Child1 class
class programmer(employee): #Inherited class.
    def __init__(self):
        super().__init__()
        print("Constructor of programmer")

    company = "Rajesh Paan waala Khan Market"

    #Non inherited function.
    def show_language(self):
        print(f"The name of the employee is {self.name}")

#Child2 class
class programmer_manager(programmer):
    def __init__(self):
        super().__init__() #Super() method. This will print the programmer class too.
        print("Constructor of programmer_manager.")

    number_of_employees_under_him = random.randint(1,100)
    
    def show_the_number_of_employees_under_him(self):
        print(f"Number of employees under him are {self.number_of_employees_under_him}")

izumi = programmer_manager()
print(izumi.company)
izumi.show("kyouko", "1rs")
izumi.show_language()
izumi.show_the_number_of_employees_under_him()
