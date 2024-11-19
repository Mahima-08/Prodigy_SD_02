import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have generated a number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        try:
            # Take user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the guess with the generated number
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function to play the game
guess_the_number()
