def greet(name, ending): 
    print(f"Hello {name} {ending}")
    return "greeted"

a = greet("Izumi", "Hope you have a nice day") 
print(a)
#If there was no return value specified in the function, the printed value of a would have been none.