3. Luhn Algorithm (Mod 10 Algorithm)
Definition:
The Luhn Algorithm is a checksum algorithm used to verify identification numbers like credit card numbers.

Steps:
Remove spaces and dashes.
Start from the right side.
Double every second digit.
If doubled value is greater than 9, subtract 9.
Add all digits.
If total is divisible by 10 → Valid.
Example:
Number:
453914889

Double alternate digits:
4 5 3 9 1 4 8 8 9
4 10 3 18 1 8 8 16 9

Reduce values:
4 1 3 9 1 8 8 7 9

Sum:
4+1+3+9+1+8+8+7+9 = 50
50 is divisible by 10:

# Luhn Algorithm

## Flow Visualization

![Luhn Algorithm](images/luhn_flow.png)


## Steps

1. Remove spaces and dashes.
2. Reverse digits.
3. Double every second digit.
4. Add all digits.
5. Check if sum is divisible by 10.

