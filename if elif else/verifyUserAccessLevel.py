# Program to verify user access level

# variable to store user role
role = input('Enter user role: ')

# displaying result to user
if role == 'admin':
    print('user has admin access rights.')
elif role == 'user':
    print('User has normal user access rights.')
else:
    print('user has guest access rights.')