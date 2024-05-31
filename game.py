import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in choices:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(choice, computer_select):
    if choice == computer_select:
        return "tie"
    elif (choice == "rock" and computer_select == "scissors") or \
         (choice == "scissors" and computer_select == "paper") or \
         (choice == "paper" and computer_select == "rock"):
        return "user"
    else:
        return "computer"

def display_result(choice, computer_select, winner):
    print(f"\nYou chose: {choice}")
    print(f"Computer chose: {computer_select}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():

    play_again = "yes"
    
    while play_again.lower() == "yes":
        choice = get_user_choice()
        computer_select = get_computer_choice()
        winner = determine_winner(choice, computer_select)
        display_result(choice, computer_select, winner)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Do you want to play again? (yes/no): ").lower()
    
    print("\nThanks for playing!")

# Run the game
play_game()
