#Input function allows you to take input from the user.
#Output is always a string

a = input("enter the first number: ")
b = input("enter the second number: ")

print(a)
print(b)

#If we print(a+b), the output wont be the sum of 2 numbers but the digits will be joined... Like 1+2=12
#This is because the output is always a string.
print("Joint of the 2 numbers is", a+b)

#To add 2 the two numbers that are given by the user:-
c = int(input("enter the first number: ")) #We put int() outside the input() which means that we are converting the string into integer.
d = int(input("enter the second number: "))
print("Sum of the two numbers is", c+d)

e = float(input("enter the decimal number: ")) #1.2 is the input
f = float(input("enter the decimal number: ")) #2.4 is the input
g = e+f
print("sum of the 2 decimal numbers is", g)
#The output will be something like 3.599999 cause of floating point precision
#To round it off, we use round(). The syntax is round(e+f,1), the one in the right stands for rounding off to 1 decimal place.
print("Sum of the two decimal numbers in rounded form is: ", round(g,1))


