from random import randint

# Constants for the number of turns based on difficulty level.
EASY_NUM_OF_TURNS = 10
HARD_NUM_OF_TURNS = 5


def check_guess(player_guess, correct_answer, turns):
    """
    Compares the player's guess with the correct answer and provides feedback.

    If the guess is too high or too low, the function prints a hint and
    decreases the turn count by one. If the guess is correct, it prints a confirmation.

    Args:
        player_guess (int): The number guessed by the player.
        correct_answer (int): The target number that needs to be guessed.
        turns (int): The current number of turns remaining.

    Returns:
        int: The updated number of turns after making the guess.
    """
    if player_guess > correct_answer:
        print("Too high.")
        return turns - 1
    elif player_guess < correct_answer:
        print("Too low.")
        return turns - 1
    else:
        print("Correct!")
        # Return the current turn count if the guess is correct.
        return turns


def set_difficulty():
    """
    Prompts the player to choose a difficulty level and returns the corresponding number of turns.

    Returns:
        int: Number of turns based on the chosen difficulty level.
    """
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_NUM_OF_TURNS
    elif difficulty == "hard":
        return HARD_NUM_OF_TURNS
    else:
        # Default to hard difficulty if the input is unrecognized.
        print("Invalid input. Defaulting to hard difficulty.")
        return HARD_NUM_OF_TURNS


def game():
    """
    Main function to run the Number Guessing Game.

    The game randomly selects a number between 1 and 100. The player is given a fixed number
    of turns to guess the number. After each guess, feedback is provided, and the number of turns
    is updated. The game ends when the player guesses correctly or runs out of turns.
    """
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate the number to guess.
    num_to_guess = randint(1, 100)

    # Determine the number of turns based on chosen difficulty.
    turns = set_difficulty()

    player_guess = None  # Initialize the player's guess.

    # Continue looping until the player guesses correctly.
    while player_guess != num_to_guess:
        print(f"\nYou have {turns} turns left.")
        player_guess = int(input("Make a guess: "))

        # Check the guess and update the number of remaining turns.
        turns = check_guess(player_guess, num_to_guess, turns)

        # If no turns remain, the game is over.
        if turns == 0:
            print("You have run out of turns, game over.")
            return
        elif player_guess != num_to_guess:
            print("Guess again.")


# Start the Number Guessing Game.
game()
