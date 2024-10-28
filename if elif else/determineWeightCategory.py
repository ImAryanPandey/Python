# Program to determine a person's weight category based on BMI

# Input for weight and height
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# displaying result to user
if bmi < 18.5:
    print('person is Underweight.')
elif 18.5 <= bmi < 24.9:
    print('person is Normal weight.')
elif 25 <= bmi < 29.9:
    print('person is Overweight.')
else:
    print('person is Obese.')

