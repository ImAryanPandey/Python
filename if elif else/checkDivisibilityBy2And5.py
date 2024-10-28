# Program to check if number is divisible by 2 and 5

# variable to store user input
num = int(input('Enter number: '))

# displaying result to user
if num % 2 == 0 and num % 5 == 0:
    print('Number is divisible by 2 and 5.')
elif num % 2 == 0:
    print('Number is divisible by 2.')
elif num % 5 == 0:
    print('Number is divisible by 5.')
else:
    print('Number is not divisible by neither 2 nor 5.')
