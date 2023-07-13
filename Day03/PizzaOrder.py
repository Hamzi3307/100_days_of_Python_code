print('WELCOME TO PYTHON PIZZA DELIVERY')

size = input('Which Size do you want (Sm,Md,Lg)? ')
pep = input('Do you want pepperoni (Y or N)? ')
cheese = input('Do you want extra cheese (Y or N)? ')
total_bill = 0
if size == 'S':
    total_bill += 15
    if pep == 'Y':
        total_bill+= 2
    if cheese=='Y':
        total_bill+=1
    print('Total Bill is: $',total_bill)
elif size == 'M':
    total_bill += 20
    if pep == 'Y':
        total_bill+= 3
    if cheese=='Y':
        total_bill+=1
    print('Total Bill is: $',total_bill)
elif size == 'L':
    total_bill += 25
    if pep == 'Y':
        total_bill+= 3
    if cheese== 'Y':
        total_bill+=1
    print('Total Bill is: $',total_bill)
else:
    print('Invalid Input')