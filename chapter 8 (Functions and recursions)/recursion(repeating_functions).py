#Recursion is a function that calls itself.

#Creating a function for factorial through recursion:-
def factorial(n): #Defining the function.
    
    if n==1 or n==0:
        return 1 #This gives python the stop value of this recursion (repeating) function. So if the value is 1/0, the function will stop repeating itself.
    
    return n * factorial(n - 1) #Return value of this function. 

num = int(input("Enter the number whose factorial you want: ")) 
factorial_value = factorial(num) #Return value gets assigned here.
print(f"The factorial of {num} is {factorial_value}") #Cant print inside the function as its repeating, the value will be printed many times.

#Lets say the num is 6
#The flow of the could is:- 
#factorial(6) = 6 x factorial(5) = 6 x 5 x factorial(4) = 6 x 5 x 4 x factorial(3) = 6 x 5 x 4 x 3 x factorial(2) = 6 x 5 x 4 x 3 x 2 x factorial(1)
#This is ultimately 6! but the function calls itself 6 times to run this code, hence the name recursion.
