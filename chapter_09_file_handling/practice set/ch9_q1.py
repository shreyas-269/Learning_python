with open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\practice set\poem.txt", "r") as f:
    poem = f.read()

poem_in_lower_case = poem.lower()

if "twinkle" in poem_in_lower_case:
    print("Yes the word twinkle is present.")
else:
    print("No the word twinkle isnt present.")


