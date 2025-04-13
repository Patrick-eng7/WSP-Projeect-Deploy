# Ask the user to enter the target number
target_number = int(input("Enter the integer for the player to guess.\n"))

# Initialize guess count
guess_count = 0
correct_guess = False

# Loop until the player guesses correctly
while not correct_guess:
    # Ask the player to enter their guess
    guess = int(input("Enter your guess.\n"))

    # Increment the guess count
    guess_count += 1

    # Check if the guess is too high, too low, or correct
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
