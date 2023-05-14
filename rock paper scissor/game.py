import random

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter your choice: (rock, paper, scissors)")
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Your choice: ").lower()
    computer_choice = random.choice(choices)
    
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("Computer wins!")
        else:
            print("You win!")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please try again.")

play_game()
