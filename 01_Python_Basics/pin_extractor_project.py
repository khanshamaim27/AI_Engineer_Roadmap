"""
PIN EXTRACTOR PROJECT
=====================

A PIN is hidden in a poem.
The nth digit of the PIN comes from the length of the nth word in the nth line.

Example:
Line 0: "Stars and the moon" → Word 0 = "Stars" (5 letters) → Digit = 5
Line 1: "shine in the sky" → Word 1 = "in" (2 letters) → Digit = 2
Line 2: "white and" → Word 2 = NOT FOUND → Digit = 0
Line 3: "until the end of the night" → Word 3 = "of" (2 letters) → Digit = 2

PIN = 5202
"""

# Step 1: Create function with parameter
def pin_extractor(poems):
    secret_codes = []
    
    # Step 17: Outer loop - iterate over all poems
    for poem in poems:
        # Step 2: Create empty string to hold the secret code
        secret_code = ''
        
        # Step 4: Split poem into lines using newline character
        lines = poem.split('\n')
        
        # Step 7: Loop through lines with enumerate to get index
        for line_index, line in enumerate(lines):
            # Step 6: Split line into words
            words = line.split()
            # Step 14: Check if there are enough words
            if len(words) > line_index:
                # Step 11: Concatenate string to secret_code using +=
                secret_code += str(len(words[line_index]))
            else:
                # Step 15: Add '0' when word is missing
                secret_code += '0'
        
        # Append secret code to list
        secret_codes.append(secret_code)
    
    # Step 12: Return the secret codes list
    return secret_codes

# Step 3: Create poem variables outside the function
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'

poem3 = 'There\nonce\nwas\na\ndragon'

# Step 13: Print the result of the function
# print(pin_extractor(poem))