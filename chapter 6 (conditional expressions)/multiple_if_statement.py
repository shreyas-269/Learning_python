age = int(input("Enter your age: "))

#If statement no. 1
if age%2==0:
    print("Age is even.")
    if age>=18:
        print("his age is driveable.")
    else:
        print("His age is non drivable.")
else:
    print("Age is odd.")

#If statement no. 2
if age>=18:
    print("You are above the age of consent.")
elif age<0:
    print("Your age is invalid.")
else:
    print("You are below the age of consent.")

#The 2 if statements will work separately and will have nothing to do with each other.