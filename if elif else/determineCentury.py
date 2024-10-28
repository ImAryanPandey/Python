# Program to determine if a given year's century

# Variable to store the year
year = int(input("Enter a year: "))

# Displaying result to user
if 1800 <= year < 1900:
    print('The year is in the 19th century.')
elif 1900 <= year < 2000:
    print('The year is in the 20th century.')
elif 2000 <= year < 2100:
    print('The year is in the 21st century.')
