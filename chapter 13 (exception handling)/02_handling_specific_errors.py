#We can handle specific types of errors specifically.
try:
    num2 = int(input("Enter the number: "))
except ValueError:
    print("Enter a valid number.")