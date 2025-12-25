import re

with open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\practice set\donkey.txt", "r+", encoding="utf-8-sig") as f:
    passage = f.read()
    updated_passage = re.sub("donkey", "######", passage, flags=re.IGNORECASE)
    f.seek(0)
    f.write(updated_passage)
    f.truncate()


    