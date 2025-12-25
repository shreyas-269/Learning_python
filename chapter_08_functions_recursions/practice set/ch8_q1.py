def greatest():
    list_of_numbers = []
    for i in range(1,4):
        num = int(input(f"Enter the {i} number: "))
    list_of_numbers.append(num)
    print(f"The greatest number is {max(list_of_numbers)}")
    
greatest()
    