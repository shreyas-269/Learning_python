num = 23
def multiplication_table():
    global num #This declares the variable num as global.
    num = int(input("Enter the number whose multiplication table you want: ")) 
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

multiplication_table()
print(num**2)

