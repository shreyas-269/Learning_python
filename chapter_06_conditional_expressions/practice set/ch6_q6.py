marks = int(input("Enter the marks: "))

if marks in range(90,100):
    print("Grade is in Ex")
elif marks in range(80,90):
    print("Grade is in A")
elif marks in range(70,80):
    print("Grade is in B")
elif marks in range(60,70):
    print("Grade is in C")
elif marks in range(50,60):
    print("Grade is in D")
else:
    print("Grade is in F")
