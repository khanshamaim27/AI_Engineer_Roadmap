"""
NUMBER PATTERN GENERATOR
========================

A function that generates a number pattern from 1 to n.

Examples:
number_pattern(4) → "1 2 3 4"
number_pattern(12) → "1 2 3 4 5 6 7 8 9 10 11 12"
"""


def number_pattern(n):
    
    #  Check if n is an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # Check if n is greater than 0
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # Use for loop to create pattern
    pattern = ""
    for i in range(1, n + 1):
        pattern += str(i) + " "
    
    # Remove the last space and return
    return pattern.strip()


# TEST CASES
print(number_pattern(4))      # Should print: 1 2 3 4
print(number_pattern(12))     # Should print: 1 2 3 4 5 6 7 8 9 10 11 12
print(number_pattern(1))      # Should print: 1
print(number_pattern(3.5))    # Should print: Argument must be an integer value.
print(number_pattern(0))      # Should print: Argument must be an integer greater than 0.
print(number_pattern(-5))     # Should print: Argument must be an integer greater than 0.