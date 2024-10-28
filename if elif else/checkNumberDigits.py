# Program to check the digits of number

# variable to store user input
num = int(input('Enter number: '))

# displaying result to user
if num < 10:
    print('Number is a one digit number.')
elif num < 100:
    print('Number is a two digit number.')
else:
    print('Number has more than two digits.')
