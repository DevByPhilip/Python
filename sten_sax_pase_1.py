import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    while True:
        player_choice = input("rock, paper or scissors? ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice, please choose rock, paper, or scissors.")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nPlayer: {player_choice}")
        print(f"Computer: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Game over!")
            break

if __name__ == "__main__":
    play_game()