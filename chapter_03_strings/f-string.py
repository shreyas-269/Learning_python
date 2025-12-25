Name = input("Your name: ")
Day = int(input("dd: "))
Month = int(input("mm: "))
Year = int(input("yyyy: ")) 
#f" is called f-string. 
#We can insert variables inside an f-string using curly brackets.
print("Dear", Name, "\nYou are selected!\nDate: ", f"{Day}/{Month}/{Year}")
