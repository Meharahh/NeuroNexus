import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose."

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}. The computer chose {computer_choice}.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    print("Welcome to the rock, paper, scissors game!")
    while True:
        play_game()
        user_response = input("Do you want to play again? Enter yes or no: ").lower()
        if user_response == "no":
            break

if __name__ == "__main__":
    main()