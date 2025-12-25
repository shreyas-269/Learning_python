def copy(file_address, copied_file_address):
    with open(file_address, "r") as f:
        content_of_text_file = f.read()
    with open(copied_file_address, "w") as f:
        f.write(content_of_text_file)

user_file_address = input("Enter your file address: ")
user_copied_file_address = input("Enter the file address where you want to copy: ")
copy(user_file_address, user_copied_file_address)
        
        