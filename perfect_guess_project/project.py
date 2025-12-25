import random
random_number = random.randint(1, 10)
number_of_tries = 0
user_guessed_number = None

while user_guessed_number != random_number:
    user_guessed_number = int(input("Guess the number: "))
    number_of_tries += 1

    if user_guessed_number>random_number:
        print("Lower")
    elif random_number>user_guessed_number:
        print("Higher")

print(f"You guessed the correct number, that is {random_number} and it took you {number_of_tries} number of tries.")




    