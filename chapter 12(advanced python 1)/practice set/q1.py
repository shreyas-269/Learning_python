try:
    with open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 12(advanced python 1)\practice set\text1.txt", "r") as f:
                        print(f.read())
    with open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 12(advanced python 1)\practice set\text2.txt", "r") as f:
                        print(f.read())
    with open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 12(advanced python 1)\practice set\text3.txt", "r") as f:
                        print(f.read())
except FileNotFoundError:
        print("File doesnt exist.")

                