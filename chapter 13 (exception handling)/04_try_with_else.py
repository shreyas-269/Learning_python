try:
    num = int(input("Enter the number: "))
except ValueError: #If the try block doesnt work, the code goes to except block.
    print("Enter a valid number.")
else: #If the try block works, the code then goes to else block.
    print(f"The square of the number is {num**2}")


    

