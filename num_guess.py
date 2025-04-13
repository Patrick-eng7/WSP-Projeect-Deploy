# Ask the user to enter the target number
target_number = int(input("Enter the integer for the player to guess.\n"))

# Initialize guess count
guess_count = 0

# Prompt the first guess
guess = int(input("Enter your guess.\n"))
guess_count += 1

# Keep looping until the guess is correct
while guess != target_number:
    if guess > target_number:
        print("Too high - try again:")
    else:
        print("Too low - try again:")

    # Get the next guess (without printing the full prompt again)
    guess = int(input())
    guess_count += 1

# Output final result
if guess_count == 1:
    print("You guessed it in 1 try.")
else:
    print(f"You guessed it in {guess_count} tries.")
