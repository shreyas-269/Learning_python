with open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\practice set\log.txt", "r") as f:
    the_whole_log = f.read()
    f.seek(0)
    
    if "python" not in the_whole_log:
        print("The word 'python' isn't in the log")
    else:
        log_list = f.readlines()
        lowered_case_log_list = []

        for log in log_list:
            lowered_log = log.lower()
            lowered_case_log_list.append(lowered_log)
    
        line_number_list = []
        for index,line in enumerate(lowered_case_log_list): #Enumerate gives the pair of (index, string) in its loop.
            if "python" in line:
                line_number = index + 1
                line_number_list.append(line_number)
        
        if len(line_number_list) == 1:
            print(f"'Python' is present on {line_number_list[0]} line.")
        elif len(line_number_list) != 1:
            line_numbers = ", ".join(str(num) for num in line_number_list)
            print(f"'Python' is present on {line_numbers} lines.")



    


            