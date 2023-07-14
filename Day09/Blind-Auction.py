from art import logo
print(logo)
bids = {}
finish = False

def winner_is(Record):
    highest_bid = 0
    winner = ''
    for bidder in Record:
        bid_amount = Record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(winner,': ',highest_bid)

while(not finish):
    name = input('Your name Please: ')
    bid = int(input('What is your bid? $'))
    bids[name] = bid
    run = input('Any Other Bidders Type Y: ').upper()
    if run=='Y':
        finish = False
    else:
        finish = True

winner_is(bids)