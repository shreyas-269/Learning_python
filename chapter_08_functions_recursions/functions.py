def avg(): #This is defining a function.
    n = int(input("How many numbers do you want averaged: "))
    
    sum = 0
    
    for i in range(1,n+1):
        num = int(input(f"enter the {i} number: "))
        sum += num
    
    average = (sum/n)
    print(f"The average is {average:.2f}")

avg() #This is calling the function.



    