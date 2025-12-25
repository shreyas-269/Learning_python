string = input("enter the string: ")
if "  " in string:
    print("present")
    print(string.replace("  ", " ")) #replacing double space with single space.
else:
    print("not present")