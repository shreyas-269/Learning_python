number = int(input("Enter the nth natural number: "))
sum = 0
i = 0

while i<=number:
    sum += i
    i += 1

print(f"The sum of the first {number} natural numbers is {sum} ")
