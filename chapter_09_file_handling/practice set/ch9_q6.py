with open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\practice set\log.txt", "r") as f:
    log = f.read()
    lowered_case_log = log.lower()
    if "python" in lowered_case_log:
        print("Yes 'python' is present in the log.")
    else:
        print("No 'python' isn't present in the log")