import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_result(user_choice, computer_choice, result):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == 'win':
        print("You win!")
    elif result == 'lose':
        print("You lose!")
    else:
        print("It's a tie!")

def rock_paper_scissors():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
        
        if user_choice == 'quit':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1
        
        display_result(user_choice, computer_choice, result)
        print(f"Score: You {user_score} - Computer {computer_score}")
        print()
    
    
    if user_score > computer_score:
        print(f"\nScore: You {user_score} - Computer {computer_score}")
        print("You won !!")
    elif user_score < computer_score:
        print(f"\nScore: You {user_score} - Computer {computer_score}")
        print("Computer won !!")
    else:
        print("\nTie !!")
        
    print()
    print("Thank you for playing!")

# Run the game
rock_paper_scissors()
