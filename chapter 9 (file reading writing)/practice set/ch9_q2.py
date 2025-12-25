def game():
    score = int(input("Enter your score: "))

    with open(r"C:\personal\shreyas\cse\code with harry python (10 hours waala oneshot)\chapter 9 (file reading writing)\practice set\game.txt", "r+") as f:
        content_of_the_file = f.read()
        if content_of_the_file == "":
            highscore = 0
        else:
            highscore = int(content_of_the_file)
        
        if score > highscore:
            f.seek(0) #This is cause the code has already read the file.
            f.write(str(score))
            f.truncate() #f.truncate() cuts off the file from the current pointer position onward.
                         #That means if the file had more data than what you just wrote, it deletes the extra part.
            print("New high score saved:", score)
        else:
            print("No new high score. Current high score:", highscore)

game()





