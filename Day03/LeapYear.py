year = int(input('Which year do you want to check: '))

while(type(year) is int):
     try:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    print('Leap Year')
                else:
                    print('Not a Leap Year')
            else:
                print('Leap Year')
        else:
            print('Not a Leap Year')
        year = int(input('Which year do you want to check: '))
     except:
        print('Exited')
        break