# Program to check if year is leap year

# variable to store user input
year = int(input('Enter year: '))

# displaying result to user
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, 'is leap year')

