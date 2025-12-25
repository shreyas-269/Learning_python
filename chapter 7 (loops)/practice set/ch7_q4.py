num = int(input("Enter the number you want to check: "))

number_of_factors = 0

if num<=1:
    print("The number is neither prime nor composite.")
else:
    for i in range(1,num+1):
        if num%i == 0:
            number_of_factors += 1 

if number_of_factors == 2:
    print("The number is prime.")
if number_of_factors > 2:
    print("The number is composite")

