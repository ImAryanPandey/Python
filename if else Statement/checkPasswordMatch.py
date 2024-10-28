# Program to check if password matches stored password.

# variable to enter stored password
storedPass = input('Enter stored password: ')
# variable to store password
password = input('Enter password: ')

# displaying result to user
if storedPass == password:
    print('Stored password matches password.')
else:
    print('Stored password does not match password.')
