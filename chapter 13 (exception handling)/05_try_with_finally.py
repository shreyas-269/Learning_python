#Usually used inside functions.
def square():
    num = None #Defining num so its available everywhere.
    
    try:
        num = int(input("Enter the number: "))
        return "fyn"
    
    except ValueError: #If the try block doesnt work, the code goes to except block.
        print("Enter a valid number.")
        return "Fyn"
    
    finally:
        if num is not None:
            print(f"The square of the number is {num**2}")
        else:
            while True:
                try:
                    num = int(input("Enter a valid number: "))
                    print(f"The square of the number is {num**2}")
                    break
                except ValueError:
                    print("Enter a valid number.")

halo = square()
print(halo)

                
        
    
