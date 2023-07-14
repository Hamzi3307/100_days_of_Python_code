import random
from art import logo
print(logo)
def compare(comp, user):
    if user == comp:
        print(f'{user} == {comp} So its Draw')
    elif user == 0:
        print(f"You Win with a BlackJack")
    elif comp == 0:
        print(f"Lose, Opponent Has BlackJack")
    elif comp > 21:
        print(f"You Win Your Score is: {user} and Computer Score is {comp}")
    elif user > 21:
        print(f"You Lose Your Score is: {user} and Computer Score is {comp}")
    else:
        if user > comp:
            print(f"You Win Your Score is: {user} and Computer Score is {comp}")
        else:
            print(f"You Lose Your Score is: {user} and Computer Score is {comp}")



def deal_card():
    """Returns Random Card from the dec"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(list):
    """Return the score of list of cards"""
    if sum(list) == 21 and len(list) == 2:
        return 0
    elif 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    u_score = calculate_score(user_cards)
    c_score = calculate_score(computer_cards)
    print(f'Your Cards are {user_cards}\nYour Current Score: {u_score}\nComputer\'s First Card: {computer_cards[0]}')
    if u_score == 0 or c_score == 0:
        is_game_over = True
    else:
        #if u_score < 22:
        draw = input('Do you want to draw another card, Type Y?').upper()
        #else:
        #    is_game_over=True
        if draw == 'Y':
            user_cards.append(deal_card())
        else:
            is_game_over = True


while c_score != 0 and c_score < 17:
    computer_cards.append(deal_card())
    c_score = calculate_score(computer_cards)
# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# is over 21, then the computer loses. If none of the above, then the player with the highest score wins.


print(user_cards, computer_cards)
compare(c_score, u_score)
