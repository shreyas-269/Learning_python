string = "\nWriting in a text file."

f = open("myfile2.txt", "a") #Opening a text file in append mode
f.write(string) #Appends at the end of the file.
f.close() #Closing it.

f = open("myfile2.txt")
print(f.read())
f.close()

print("\nThe output of file 3 will be shown in the next line.")

f = open("myfile3.txt", "a") #Append also creates a new file if it doesnt already exists.
f.write(string)
f.close()

f = open("myfile3.txt")
print(f.read())
f.close()
