def hcf():
    s1 = set()
    s2 = set()

    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    for i in range(1,n1+1):
        if n1%i==0:
            s1.add(i)

    for j in range(1,n2+1):
        if n2%j==0:
            s2.add(j)

    s3 = s1.intersection(s2)
    print(f"The hcf is {max(s3)}")

hcf()