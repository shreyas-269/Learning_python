f = open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\O)\file.txt", "r") 
#Opening a file.
#We used r"file location" because copy pasting the whole file path will always work irrespective of where the file path is.
#r"" is used for raw strings. \ is treated like an esacpe sequence character like \n etc in a normal string, but not in a raw string.
print(f.read()) #Printing the content of a file.
f.close() #Closing a file.

#Opening a text file syntax :-
# open(r"file path", mode of opening the file)
#Mode of opening the file is bydefault read so we dont have to type open("file path", "r")


