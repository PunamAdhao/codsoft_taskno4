"""User Input: Prompt the user to choose rock, paper, or scissors.
 Computer Selection: Generate a random choice (rock, paper, or scissors) for
 the computer.
 Game Logic: Determine the winner based on the user's choice and the
 computer's choice.
 Rock beats scissors, scissors beat paper, and paper beats rock.
 Display Result: Show the user's choice and the computer's choice.
 Display the result, whether the user wins, loses, or it's a tie.
 Score Tracking (Optional): Keep track of the user's and computer's scores for
 multiple rounds.
 Play Again: Ask the user if they want to play another round.
 User Interface: Design a user-friendly interface with clear instructions and
 feedback"""

import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Choose rock, paper, or scissors. Type 'exit' to quit.")

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == 'exit':
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}")
        print()  # Print a blank line for better readability

    print("Thanks for playing! Final Scores -> You: {}, Computer: {}".format(user_score, computer_score))

if __name__ == "__main__":
    main()
