num = int(input("Enter the number whose factorial you want: "))

factorial = 1

for i in range(1,num+1):
    factorial *= i
    i += 1

print(f"The factorial is {factorial}")


