target_number = int(input("Enter the integer for the player to guess.\n"))

guess_count = 0
correct_guess = False

while not correct_guess:

    guess = int(input("Enter your guess.\n"))

    guess_count += 1
    if guess > target_number:
        print("Too high - try again:")
    elif guess < target_number:
        print("Too low - try again:")
    else:
        correct_guess = True
        if guess_count == 1:
            print(f"You guessed it in 1 try.")
        else:
            print(f"You guessed it in {guess_count} tries.")
