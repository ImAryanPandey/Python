# Program to determine if a person is a child, adolescent, or adult based on age

# Variable to store age
age = int(input("Enter age: "))

# Displaying result to user
if age < 0:
    print('Invalid age.')
elif age <= 12:
    print('The person is a Child.')
elif age <= 19:
    print('The person is an Adolescent.')
else:
    print('The person is an Adult.')
