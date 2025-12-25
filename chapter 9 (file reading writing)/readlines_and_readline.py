#readlines() returns a list of all the lines in it.
f = open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\readlines.txt") 
print(f.readlines())
f.close()

#readline() returns a string that has one single line of that txt file.

#Printing all the lines manually.
f = open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\readlines.txt")
line1 = (f.readline()) #This reads the line 1 and the pointer goes to the next line.
line2 = (f.readline()) #This reads the line 2 and the pointer goes to the next line.
line3 = (f.readline()) #This reads the line 3 and the pointer goes to the next line.
line4 = (f.readline()) #This reads the line 4 and the pointer goes to the next line.
print(line1)
print(line2)              
print(line3)
print(line4)

f.seek(0) #Bringing the pointer back to top.

print("The new output starts in the next line. \n")

#Printing all the lines using for loop.
for i in range(1,5):
    print(f.readline())

print("The new output starts in the next line. \n")

f.seek(0) #Bringing the pointer back to top.

#Printing all the lines using while loop.
i = 1
while i<=4:
    print(f.readline())
    i += 1

print("The new output starts in the next line. \n")

f.seek(0) #Bringing the pointer back to top.

#Printing all the lines using while loop with != method.
line = f.readline() #Reads the first line.
while line != "": #Run the loop till the line doesnt get an empty string through readline()
    print(line, end = "") #The line is printed and the pointer doesnt go to the next line cause of the while loop.
    line = f.readline() #Now the pointer goes to the next line and the line is readed.

f.close()