# Program to determine a person's life stage based on age

# Variable to store age
age = int(input('Enter user age: '))

# Displaying result to user
if age < 0:
    print('Invalid age.')
elif age <= 12:
    print('The person is a Child.')
elif age <= 19:
    print('The person is a Teen.')
elif age <= 64:
    print('The person is an Adult.')
else:
    print('The person is a Senior.')
