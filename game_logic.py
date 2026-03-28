import random
from constants import CHOICES_NAMES

# Maps each choice to what it beats
WINS_AGAINST = {'r': 's', 's': 'p', 'p': 'r'}


def is_win(player, opponent):
    return WINS_AGAINST.get(player) == opponent


def play(user_choice):
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif is_win(user_choice, computer_choice):
        result = "You won!"
    else:
        result = "You lost!"

    return result, computer_choice


def get_choice_name(choice):
    """Return the display name for a choice key."""
    return CHOICES_NAMES.get(choice, "Unknown")
