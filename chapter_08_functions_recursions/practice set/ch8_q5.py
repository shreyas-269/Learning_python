def star_printing():
    n = int(input("Enter the number of rows of stars you want: "))

    for i in range(1,n+1):
        print("*" * (n+1-i))

star_printing()