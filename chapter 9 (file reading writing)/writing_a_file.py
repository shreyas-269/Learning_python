string = "Writing in a text file"

f = open("myfile.txt", "w") #Opening a text file in write mode.
#This creates a text file if that text file isn't already present.
f.write(string) #Writing inside a text file.
f.close() #Closing it.

f = open("myfile.txt")
print(f.read())
f.close()
