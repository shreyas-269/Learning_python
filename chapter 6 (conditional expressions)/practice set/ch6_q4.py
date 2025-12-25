username = input("Enter the username: ")

if len(username)<10:
    print("Username has less than 10 letters.")
elif len(username)==10:
    print("Username has 10 letters.")
else:
    print("Username has more than 10 letters")
