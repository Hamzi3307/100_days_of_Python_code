def check_resourses(item, stock):


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

off = False

while (not off):
    user_input = input("What would you like? (espresso/latte/cappuccino):").upper()
    if user_input == 'OFF':
        print('Turned Off')
        off = True
    elif user_input == 'REPORT':
        resources['Money $'] = money
        print(resources)
        continue
    elif user_input in MENU.keys():
        check_resourses(user_input,resources)
