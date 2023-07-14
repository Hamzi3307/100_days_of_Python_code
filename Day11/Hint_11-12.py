import random
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

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated
# until the game ends.
while not is_game_over:
    u_score = calculate_score(user_cards)
    c_score = calculate_score(computer_cards)
    print(f'Your Cards are {user_cards}\nYour Current Score: {u_score}\nComputer\'s First Card: {computer_cards[0]}')
    if u_score == 0 or c_score == 0:
        is_game_over = True
    else:
        draw = input('Do you want to draw another card, Type Y?').upper()
        if draw == 'Y':
            user_cards.append(deal_card())
        else:
            is_game_over = True
# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long
# as it has a score less than 17.
while c_score!=0 and c_score < 17:
    computer_cards.append(deal_card())
    c_score = calculate_score(computer_cards)

print(computer_cards, user_cards)
