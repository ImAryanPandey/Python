# Program to assign a performance rating based on a percentage

# Variable to store the percentage
percentage = float(input("Enter the percentage: "))

# Displaying result to user
if percentage >= 90:
    print('Performance Rating: Excellent')
elif percentage >= 75:
    print('Performance Rating: Good')
elif percentage >= 50:
    print('Performance Rating: Average')
else:
    print('Performance Rating: Poor')
