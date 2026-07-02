"""
==========================================
Day 05 - Error Handling Practice
==========================================

Instructions:

Your task is to fix every bug.

Do NOT look at the solution first.

Topics:
- try
- except
- else
- finally
- raise

Good Luck!
"""

print("========== Challenge 1 ==========")

# BUG 1
# User enters two numbers.
# Prevent the program from crashing if
# the second number is zero.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 / num2)


print("\n========== Challenge 2 ==========")

# BUG 2
# Handle invalid integer input.

age = int(input("Enter your age: "))

print(f"You are {age} years old.")


print("\n========== Challenge 3 ==========")

# BUG 3
# Prevent List Index Error.

colors = ["Red", "Green", "Blue"]

index = int(input("Choose index (0-2): "))

print(colors[index])


print("\n========== Challenge 4 ==========")

# BUG 4
# Handle wrong data type.

numbers = [10, 20, 30]

position = input("Enter list position: ")

print(numbers[position])


print("\n========== Challenge 5 ==========")

# BUG 5
# Use raise to stop negative ages.

age = int(input("Enter age: "))

if age < 0:
    # Write raise statement here
    pass

print("Age accepted.")


print("\n========== Challenge 6 ==========")

# BUG 6
# Use else and finally correctly.

number = int(input("Enter a number: "))

print(100 / number)