# Program to classify temperature

# variable to store temperature
temp = int(input('Enter temperature: '))

# displaying result to user
if temp > 35:
    print('Temperature is hot.')
elif 10 <= temp < 35:
    print('Temperature is warm')
else:
    print('Temperature is cold.')
