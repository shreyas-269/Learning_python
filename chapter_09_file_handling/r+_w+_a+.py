#r+
#Stands for read + write.
#File must already exist.
#Doesn't erase the file if it already exists.

f = open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\r+.txt", "r+")
f.seek(5)
f.write(" oh mae gawdd ") #Writing in r+ overwrites after the 5th index, it doesnt insert the stuff between it.
f.seek(0)
print(f.read())
f.close()

#w+
#Read as write + read.
#File gets erased first and then you can replace it with the new content.
#If file exists, contents are erased and new contents are added.
#If file doesnt exist, new file is created. 
f = open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\w+.txt", "w+")
f.write("The contents of this file have been overwritten.")
f.seek(0)
print(f.read())
f.close()

#a+
#Append + read
#Opens the file if it exists, creates a new one if it doesnt.
f = open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\a+.txt", "a+")
f.write("\nThe new appended line.")
f.seek(0)
print(f.read())
f.close()

