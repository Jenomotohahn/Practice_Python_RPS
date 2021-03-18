import random


def play():
    is_valid = False
    computer = random.choice(["r", "p", "s"])

    while is_valid == False:
        user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
        is_valid = check_input(user)

    if user == computer:
        return "tie"
    if is_win(user, computer) == True:
        return f"You win! Computer had {computer}"

    return "Computer wins..boo"


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


def check_input(user_input):
    choices = ["r", "s", "p"]
    set_choice = set(choices)
    if user_input in set_choice:
        return True
    else:
        return False


print(play())
