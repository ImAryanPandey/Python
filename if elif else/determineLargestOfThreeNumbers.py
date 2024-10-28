# Program to determine largest of three numbers

# variables to store user inputs
num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
num3 = int(input('Enter number 3: '))

# displaying result to user
if num1 > num2 and num1 > num3:
    print(num1, 'is the largest.')
elif num2 > num1 and num2 > num3:
    print(num2, 'is the largest.')
else:
    print(num3, 'is the largest.')
