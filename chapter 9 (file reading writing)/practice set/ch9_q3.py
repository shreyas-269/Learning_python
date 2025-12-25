import os

# Make sure the folder exists
folder_path = r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\practice set\multiplication tables"
os.makedirs(folder_path, exist_ok=True)

for i in range(2,21):
    with open(fr"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\practice set\multiplication tables\table_of_{i}.txt", "w") as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n")
            
