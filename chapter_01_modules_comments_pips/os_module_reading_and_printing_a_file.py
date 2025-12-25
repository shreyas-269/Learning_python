import os 

# specify the directory you want to list
directory_path="C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 1 (module, comments and pips)"

# list all files and directories in the specified path using the os module
contents=os.listdir(directory_path)

print(contents)

# print each file and directory name 
for item in contents:
    print(item)
    



