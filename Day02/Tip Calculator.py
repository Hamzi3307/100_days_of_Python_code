print('Welcome to the Tip Calculator')

bill = float(input('What was the total bill? $'))

tipPrcntg = int(input('What Percentage tip 10, 12 or 15? '))

members = int(input('How many are you to split the bill? '))

total_tip = (tipPrcntg/100) * bill

total_bill = bill + total_tip

print('Each Person should pay $',total_bill/members)

print('Total Bill with Tip is $', total_bill)

print('Tip is: $', total_tip)