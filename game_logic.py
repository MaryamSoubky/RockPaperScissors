import random

def play(user_choice):
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif is_win(user_choice, computer_choice):
        result = "You won!"
    else:
        result = "You lost!"

    return result, computer_choice

def is_win(player, opponent):
     # return true if player wins
     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
         return True