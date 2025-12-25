class calculator():
    @staticmethod
    def greet():
        print("Hello user.")
        
    def square(self, number):
        square_of_the_number = number**2
        print(f"Square of the number is {square_of_the_number}")
    
    def cube(self, number):
        cube_of_the_number = number**3
        print(f"Cube of the number is {cube_of_the_number}")
    
    def square_root(self, number):
        square_root_of_the_number = number**0.5
        print(f"Square root of the number is {square_root_of_the_number}")

def using_the_calculator():
    user_chosen_number = int(input("Enter the number you want to operate with: "))

    #Creating a menu
    any_calculator = calculator()
    any_calculator.greet()
    print("For square, choose 1.")
    print("For cube, choose 2.")
    print("For square root, choose 3.")

    the_operation_that_user_wants = int(input("Enter the mathematical operation you want by choosing a number between 1 and 3: "))
    if the_operation_that_user_wants>=1 and the_operation_that_user_wants<=3:
        if the_operation_that_user_wants==1:
            any_calculator.square(user_chosen_number)
        elif the_operation_that_user_wants==2:
            any_calculator.cube(user_chosen_number)
        elif the_operation_that_user_wants==3:
            any_calculator.square_root(user_chosen_number)
    else:
        print("There is no mathematical operation for this number.")

using_the_calculator()
    
