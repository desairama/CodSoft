import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def main():
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors game!")
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print("Final Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print(f"\nYour choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
            
        print(f"Scores - You: {user_score}, Computer: {computer_score}\n")

if __name__ == "__main__":
    main()
