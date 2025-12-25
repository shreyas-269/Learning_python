#If you write a code and it doesnt work cause of some error, you use "try" to try that code out and show something else as error rather than letting the whole program crash.
try:
    num1 = int(input("Enter the number: "))
except Exception as e:
    print(e)
    

