import random # importing random  to choose random value form given 

def get_computer_choice(): # creating a get_computer_choice() function 
    choices = ['rock', 'paper', 'scissors'] # we create a list who contains 'rock', 'paper', 'scissors'. 
    return random.choice(choices) # it will return a random value from list whose name is choices

def determine_winner(user_choice, computer_choice):  # creating a determine_winner() which determine the winner of the rounds.
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_result(user_choice, computer_choice, result): # it will create a display_result() function to display the result of the matches
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == 'win':
        print("You win!")
    elif result == 'lose':
        print("You lose!")
    else:
        print("It's a tie!")

def rock_paper_scissors(): # this function will determine that how many times the user or computer wins
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()
        
        if user_choice == 'quit':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice() # it will call get_computer_choice() and store result in 'computer_choice' variable
        result = determine_winner(user_choice, computer_choice) # it will call determine_winner and store result in 'result' variable
        
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1
        
        display_result(user_choice, computer_choice, result) # it will display the result of match rounds  
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
rock_paper_scissors() # here we calling the main function rock_paper_scissors()
