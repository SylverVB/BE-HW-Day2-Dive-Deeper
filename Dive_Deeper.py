# Lesson 2: The Magic of Conditional Statements: 
# Assignments: Dive Deeper

# 1. Decisions at the Crossroad
# Task 1: Code Correction

# Correct Code:

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# 2. The Greatest Showdown

number1 = float(input("Enter a number one: "))      # We can also use int(input("Enter a number one: ")), but it won't work with float numbers
number2 = float(input("Enter a number two: "))      # We can also use int(input("Enter a number one: ")), but it won't work with float numbers
number3 = float(input("Enter a number three: "))    # We can also use int(input("Enter a number one: ")), but it won't work with float numbers

# Task 1: Identify the Greatest
if number1 >= number2 and number1 >= number3:
    print(f'The largest number is {number1}.')
elif number2 >= number1 and number2 >= number3:
    print(f'The largest number is {number2}.')
elif number3 >= number1 and number3 >= number2:
    print(f'The largest number is {number3}.')

# Task 2: Identify the Smallest
if number1 <= number2 and number1 <= number3:
    print(f'The smallest number is {number1}.')
elif number2 <= number1 and number2 <= number3:
    print(f'The smallest number is {number2}.')
elif number3 <= number1 and number3 <= number2:
    print(f'The smallest number is {number3}.')