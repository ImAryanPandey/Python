# Program to check if a month belongs to a season

# Variable to store month
month = input("Enter the month: ")

# Displaying result to user
if month in ['december', 'january', 'february']:
    print('The month belongs to Winter.')
elif month in ['march', 'april', 'may']:
    print('The month belongs to Spring.')
elif month in ['june', 'july', 'august']:
    print('The month belongs to Summer.')
elif month in ['september', 'october', 'november']:
    print('The month belongs to Fall.')
else:
    print('Invalid month. Please enter a valid month name.')
