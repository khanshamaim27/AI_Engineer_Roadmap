"""
DAY 3: LOOPS AND CONDITIONALS
==============================

In this file you will learn:
1. if, elif, else - Making decisions in your code
2. for loops - Repeating code a specific number of times
3. while loops - Repeating code while a condition is true
4. break and continue - Controlling loop flow

These are fundamental programming concepts!
"""

print("=" * 70)
print("SECTION 1: IF, ELIF, ELSE (CONDITIONAL STATEMENTS)")
print("=" * 70)

print("\n--- Simple if Statement ---")
# if checks if a condition is True
age = 20
if age >= 18:
    print(f"Age is {age}: You are an adult!")

print("\n--- if-else Statement ---")
# if-else: do one thing if True, another if False
score = 45
if score >= 50:
    print(f"Score {score}: PASS")
else:
    print(f"Score {score}: FAIL")

print("\n--- if-elif-else Statement ---")
# elif = "else if" - check multiple conditions
marks = 75
if marks >= 90:
    grade = "A"
    print(f"Marks: {marks}, Grade: {grade} (Excellent)")
elif marks >= 80:
    grade = "B"
    print(f"Marks: {marks}, Grade: {grade} (Very Good)")
elif marks >= 70:
    grade = "C"
    print(f"Marks: {marks}, Grade: {grade} (Good)")
elif marks >= 60:
    grade = "D"
    print(f"Marks: {marks}, Grade: {grade} (Pass)")
else:
    grade = "F"
    print(f"Marks: {marks}, Grade: {grade} (Fail)")

print("\n--- Comparison Operators ---")
# These are used in conditions
x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y (equal): {x == y}")      # False
print(f"x != y (not equal): {x != y}")  # True
print(f"x < y (less than): {x < y}")    # True
print(f"x > y (greater than): {x > y}") # False
print(f"x <= y (less or equal): {x <= y}")  # True
print(f"x >= y (greater or equal): {x >= y}")  # False

print("\n--- Logical Operators (and, or, not) ---")
# Combine multiple conditions

age = 20
has_license = True

# and: both conditions must be True
if age >= 18 and has_license:
    print("You can drive!")

# or: at least one condition must be True
is_weekend = True
has_holiday = False
if is_weekend or has_holiday:
    print("You can relax today!")

# not: reverses the condition
is_raining = False
if not is_raining:
    print("Weather is good for going outside!")

print("\n" + "=" * 70)
print("SECTION 2: FOR LOOPS (REPEAT CODE N TIMES)")
print("=" * 70)

# for loop repeats code a specific number of times
# It goes through each item in a collection

print("\n--- Simple for Loop ---")
# Repeat code a certain number of times
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(f"Iteration {i}")

print("\n--- for Loop with List ---")
# Loop through each item in a list
fruits = ["Apple", "Banana", "Orange", "Mango"]
print("My favorite fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

print("\n--- for Loop with String ---")
# Loop through each character in a string
word = "PYTHON"
print(f"Letters in '{word}':")
for letter in word:
    print(f"  {letter}")


print("\n--- for Loop with enumerate() ---")
# enumerate() gives you both the index and the item
languages = ["Python", "JavaScript", "Java", "C++"]
print("Programming languages:")
for index, language in enumerate(languages):
    print(f"  {index + 1}. {language}")

print("\n--- for Loop with range() ---")
# range(start, end, step)
print("Numbers 0 to 9:")
for num in range(10):
    print(num, end=" ")
print()  # New line

print("\nNumbers 1 to 10:")
for num in range(1, 11):
    print(num, end=" ")
print()

print("\nEven numbers 0 to 10:")
for num in range(0, 11, 2):
    print(num, end=" ")
print()

print("\n--- Nested for Loop ---")
# Loop inside a loop
print("Multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()  # New line

print("\n" + "=" * 70)
print("SECTION 3: WHILE LOOPS (REPEAT WHILE CONDITION IS TRUE)")
print("=" * 70)

# while loop repeats while a condition is True
# It stops when the condition becomes False

print("\n--- Simple while Loop ---")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment count (count = count + 1)

print("\n--- while Loop with Input ---")
# This could ask user for input (we'll keep it simple)
number = 0
print("Counting up from 0:")
while number < 5:
    print(number, end=" ")
    number += 1
print()

print("\n--- while Loop Example: Guessing Game ---")