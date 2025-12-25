def sum_of_first_n_natural_numbers(n):
    if n==1:
        return 1
    return n + sum_of_first_n_natural_numbers(n-1)

n = int(input("Enter the number of natural numbers you want to add: "))
print(f"The sum of first {n} natural numbers is {sum_of_first_n_natural_numbers(n)}")

