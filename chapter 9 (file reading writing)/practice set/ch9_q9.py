def content_copy_checker(file1_address, file2_address):
    with open(file1_address, "r") as f:
        content1 = f.read()
    with open(file2_address, "r") as f:
        content2 = f.read()
    if content1 == content2:
        print("Both files contain the same contents.")
    else:
        print("They are different.")

file1 = input("Enter the address of the 1st file: ")
file2 = input("Enter the address of the 2nd file: ")

content_copy_checker(file1, file2)
