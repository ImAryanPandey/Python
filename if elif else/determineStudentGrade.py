# Program to determine grades

# variable to store user input
marks = int(input('Enter student marks: '))

# displaying result to user
if marks >= 75:
    print('grade: A')
elif 65 <= marks < 75:
    print('grade: B')
elif 55 <= marks < 65:
    print('grade: C')
elif 50 <= marks < 55:
    print('grade: D')
else:
    print('grade: F')