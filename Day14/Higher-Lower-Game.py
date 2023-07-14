import random
from game_data import data
from art import logo, vs

print(logo)
total = 0
p1 = random.randint(0, len(data) - 1)
p2 = random.randint(0, len(data) - 1)
game_over = False

while not game_over:
    print(f"Compare A:  {data[p1]['name']}, a {data[p1]['description']}, from {data[p1]['country']}")
    print(vs)
    print(f"Against B:  {data[p2]['name']}, a {data[p2]['description']}, from {data[p2]['country']}")

    guess = input('Which one has more followers A or B').upper()
    check = data[p1]['follower_count'] >= data[p2]['follower_count']
    if check and guess == 'A':
        total += 1
    elif not check and guess == 'B':
        total += 1
    else:
        print(f'Finished Your Score is: {total}')
        game_over = True
        break
    p1 = p2
    p2 = random.randint(0, len(data) - 1)


print(f'Finished Your Score is: {total}')
