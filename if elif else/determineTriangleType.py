# Program to determine triangle type

# variable to store triangle sides
side1 = float(input('Enter triangle side 1: '))
side2 = float(input('Enter triangle side 2: '))
side3 = float(input('Enter triangle side 3: '))

# displaying result to user
if side1 == side2 == side3:
    print('The triangle is Equilateral.')
elif (side1 == side2) or (side2 == side3) or (side3 == side1):
    print('The triangle is Isosceles.')
else:
    print('The triangle is scalene.')
