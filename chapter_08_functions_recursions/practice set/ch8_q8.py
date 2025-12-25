def multiplication_table():
    num = int(input("Enter the number whose multiplication table you want: "))
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

multiplication_table()