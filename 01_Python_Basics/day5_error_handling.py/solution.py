"""
Solution File
"""

print("========== Challenge 1 ==========")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 / num2)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

print("\n========== Challenge 2 ==========")

try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old.")

except ValueError:
    print("Invalid age.")

print("\n========== Challenge 3 ==========")

colors = ["Red", "Green", "Blue"]

try:
    index = int(input("Choose index (0-2): "))
    print(colors[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Enter a number.")

print("\n========== Challenge 4 ==========")

numbers = [10, 20, 30]

try:
    position = int(input("Enter list position: "))
    print(numbers[position])

except Exception as e:
    print(e)

print("\n========== Challenge 5 ==========")

try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age accepted.")

except ValueError as e:
    print(e)

print("\n========== Challenge 6 ==========")

try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

else:
    print("Everything worked successfully.")

finally:
    print("Program Finished.")