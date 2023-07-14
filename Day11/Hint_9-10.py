import random
def deal_card():
    """Returns Random Card from the dec"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list):
    """Return the score of list of cards"""
    if sum(list) == 21 and len(list)==2:
        return 0

    elif 11 in list and sum(list)>21:
        list.remove(11)
        list.append(1)
    return sum(list)

user_cards = []
computer_cards = []
is_game_over=False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
print(computer_cards,user_cards)


#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
if calculate_score(user_cards) == 0 or calculate_score(computer_cards)==0:
    is_game_over = True

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card()
# function to add another card to the user_cards List. If no, then the game has ended.
else:
    draw = input('Do you want to draw another card, Type Y?').upper()
    if draw == 'Y':
        user_cards.append(deal_card())
    else:
        is_game_over=True

print(computer_cards,user_cards)
