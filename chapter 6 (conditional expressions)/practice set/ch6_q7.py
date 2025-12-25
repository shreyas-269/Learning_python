passage = "Write a program to find out whether a given post is talking about Harry or not."

if "Harry".lower() in passage.lower(): #This is done so that if a guy write harRy in the passage, that can also be detected.
#lower() converts everything into lower case.
    print("Convo is about harry")
else:
    print("Convo is not about harry")


