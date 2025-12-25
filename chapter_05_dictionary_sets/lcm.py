def lcm():
    n1 = int(input("Enter the 1st number: "))
    n2 = int(input("Enter the 2nd number: "))

    s1 = set()
    s2 = set()

    for i in range(1,n2+1):
        s1.add(n1*i)
    for j in range(1,n1+1):
        s2.add(n2*j)

    s3 = s1.intersection(s2)
    print(f"The lcm is {min(s3)} ")

lcm()



