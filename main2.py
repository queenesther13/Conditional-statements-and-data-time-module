height = float(input('Enter your height in metres:'))
weight = float(input('Enter your weight in kg:'))
BMI = weight/(height**2)
print('your BMI is: ',BMI)
if BMI <=18.4:
    print('you are underweight')
elif BMI <=24.9:
    print('you are healthy')
elif BMI <=29.9:
    print('you are overweight')
elif BMI <=39.9:
    print('you are obese')
else:
    print('Invalid input')