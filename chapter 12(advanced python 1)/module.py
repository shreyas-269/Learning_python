def func():
    print("Halo")
def greet():
    print("Good morning")
func()
greet()
print(__name__) #__name__ here will tell main as this is the source file.

if __name__ == "__main__":
    print("We are executing the source file. The output of the file is produced by the code inside the file and no code from outside has been taken.")
