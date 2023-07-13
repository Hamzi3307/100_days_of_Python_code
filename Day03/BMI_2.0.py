print('BMI CALCULATOR')

height = float(input('Input your height in meters: '))
weight = float(input('Input your weght in kilo: '))

BMI = (weight)/(height**2)

print('Your BMI : {:.2f}'.format(BMI))

if BMI<18.5:
    print('Your are UnderWeight')
elif BMI<25:
    print('You have Normal Weight')
elif BMI<30:
    print('Your are OverWeight')
elif BMI<35:
    print('You are Obese')
else:
    print('You are Clinically Obese')
