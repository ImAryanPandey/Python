# Program to determine if a given time is morning, afternoon, or evening

# Variable to store the hour
hour = int(input("Enter the hour (0-23): "))

# Displaying result to user
if hour < 0 or hour > 23:
    print('Invalid hour. Please enter a value between 0 and 23.')
elif hour < 12:
    print('It is Morning.')
elif hour < 18:
    print('It is Afternoon.')
else:
    print('It is Evening.')
