def greet(name, ending = "Hope you have a nice day."): #Here "I hope...." is the default parameter value of that argument. 
    print(f"Hi {name}")
    print(ending) 

greet("Izumi") #The value of the argument 'ending is not given so python will take the default value as the value of the argument.
greet("Izumi", "Would you like to have a cup of coffee?") #Now the value of ending is given so it will take this one.

