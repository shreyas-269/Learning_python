#We can also raise an error with a message printed along with it.
a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))
if b==0:
    raise ZeroDivisionError("The denominator cant be 0.") #This gives a customized error.
else:
    print(f"The output of division is {a/b}")
#We deliberately use raise an error so that the developer that will use this code in future doesnt use it incorrectly.