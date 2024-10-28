# Program to determine number size

# variable to store user input
num = int(input('Enter number: '))

# displaying result to user
if num > 10000:
    print('Number is large.')
elif 100 <= num <= 10000:
    print('Number is medium.')
else:
    print('Number is small.')
