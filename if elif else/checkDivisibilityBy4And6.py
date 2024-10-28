# Program to check if number is divisible by 4 and 6

# variable to store user input
num = int(input('Enter number: '))

# displaying result to user
if num % 4 == 0 and num % 6 == 0:
    print('Number is divisible by 4 and 6.')
elif num % 4 == 0:
    print('Number is divisible by 4.')
elif num % 6 == 0:
    print('Number is divisible by 6.')
else:
    print('Number is not divisible by neither 4 nor 6.')
