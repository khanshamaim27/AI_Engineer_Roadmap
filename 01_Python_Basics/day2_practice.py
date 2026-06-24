"""
DAY 2: STRINGS, LISTS, AND TUPLES
==================================

In this file you will learn:
1. Strings - Text data and string methods
2. Lists - Multiple items collection (changeable)
3. Tuples - Multiple items collection (unchangeable)

Each concept has examples that you can run and understand.
"""
print("=" * 60)
print("SECTION 1: STRINGS (TEXT DATA)")
print("=" * 60)

# String is text enclosed in quotes
# You can use single quotes or double quotes - both are same

name="shamaim khan"
city="Faisalabad"

print(f'Name:{name}')# Store string in variable and use it
print(f'Name:{city}') # f-string allows us to put variables inside {} in a string

print("\n--- String Length ---")
# len() function gives us the length (number of characters) of a string
text = "Hello"
print(f"Text: '{text}'")
print(f"Length: {len(text)}")  # 5 characters

print("\n--- String Methods (Built-in Functions) ---")
# Strings have many useful methods we can use
message = "Shamaim is the best"
# .upper() - converts all letters to uppercase
print(f"Orignal:{message}")
print(f"Uppercase:{message.upper()}")

# .lower() - converts all letters to lowercase
TEXT = "SHAMAIM IS THE BEST"
print(f"Original: {TEXT}")
print(f"Lowercase: {TEXT.lower()}")

# .replace() - replaces one text with another
old_text = "I like Java"
new_text = old_text.replace("Java", "Python")
print(f"Original: {old_text}")
print(f"Replaced: {new_text}")

print("\n--- String Slicing (Extract Parts) ---")
# Slicing helps us get specific parts of a string
# Format: string[start:end:step]
# Note: The end index is NOT included

word = "Python"
print(f"Original word: {word}")
print(f"word[0]: {word[0]}")      # First character: P
print(f"word[1]: {word[1]}")      # Second character: y
print(f"word[-1]: {word[-1]}")    # Last character: n
print(f"word[:3]: {word[:3]}")    # First 3 characters: Pyt
print(f"word[2:5]: {word[2:5]}")  # Characters from index 2 to 5: tho

print("\n--- String Concatenation (Joining) ---")
# Join two strings together
first_name = "Shamaim"
last_name = "khan"
full_name = first_name + " " + last_name
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Full name: {full_name}")

print("\n" + "=" * 60)
print("SECTION 2: LISTS (ORDERED COLLECTION - CHANGEABLE)")
print("=" * 60)

# List is multiple items inside square brackets []
# Lists are MUTABLE - you can change them
fruits=["Apple","Banana","orange"]
print(f"lists:{fruits}")
print(f"Type: {type(fruits)}")  # <class 'list'>

print("\n--- Accessing List Items ---")
# Each item in a list has an index (position)
# Index starts from 0 (first item)

print(f"First fruit (index 0): {fruits[0]}")      # Apple
print(f"Second fruit (index 1): {fruits[1]}")     # Banana

print("\n--- List Length ---")
# len() tells us how many items are in the list
print(f"Total fruits: {len(fruits)}")  # 4

print("\n--- Adding Items to List (append) ---")
# .append() adds new item at the end of the list
print(f"Before: {fruits}")
fruits.append("Grapes")
fruits.append("Strawberry")
print(f"After: {fruits}")

print("\n--- Removing Items from List (remove) ---")
# .remove() removes a specific item
print(f"Before: {fruits}")
fruits.remove("Banana")  # Banana will be removed
print(f"After removing Banana: {fruits}")

print("\n--- Inserting Items at Specific Position (insert) ---")
# .insert(index, item) - add item at specific position
print(f"Before: {fruits}")
fruits.insert(1, "Watermelon")  # Add Watermelon at index 1
print(f"After inserting Watermelon at index 1: {fruits}")

print("\n--- List Slicing ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers}")
print(f"First 5 items [0:5]: {numbers[0:5]}")      # [1, 2, 3, 4, 5]
print(f"Last 3 items [-3:]: {numbers[-3:]}")       # [8, 9, 10]
print(f"Every 2nd item [::2]: {numbers[::2]}")     # [1, 3, 5, 7, 9]
print(f"Reverse [::-1]: {numbers[::-1]}")          # [10, 9, 8, ...]

print("\n--- Iterating Through List (Loop) ---")
# for loop lets us go through each item in the list
print("Fruits in my list:")
for fruit in fruits:
    print(f"  - {fruit}")

print("\n--- List with Different Data Types ---")
# Lists can contain different types of data
mixed_list = ["Hello", 25, 3.14, True, None]
print(f"Mixed list: {mixed_list}")
for item in mixed_list:
    print(f"  Item: {item}, Type: {type(item)}")


print("\n" + "=" * 60)
print("SECTION 3: TUPLES (ORDERED COLLECTION - UNCHANGEABLE)")
print("=" * 60)

# Tuple is like a list but uses parentheses ()
# Tuples are IMMUTABLE - you cannot change them

colors = ("Red", "Green", "Blue", "Yellow")
print(f"Tuple: {colors}")
print(f"Type: {type(colors)}")  # <class 'tuple'>

print("\n--- Accessing Tuple Items ---")
# Access tuple items just like lists
print(f"First color: {colors[0]}")    # Red
print(f"Last color: {colors[-1]}")    # Yellow
print(f"Length: {len(colors)}")       # 4

print("\n--- Tuple Unpacking ---")
# You can unpack tuple items into separate variables
color1, color2, color3, color4 = colors
print(f"Unpacked:")
print(f"  color1 = {color1}")
print(f"  color2 = {color2}")
print(f"  color3 = {color3}")
print(f"  color4 = {color4}")

print("\n--- Why Tuple? (Immutable) ---")
# Tuples cannot be changed - this makes them safe
print("Trying to change a tuple:")
print("  (You cannot change tuple items)")
# colors[0] = "Pink"  # This would give an error!


print("\n--- List vs Tuple Comparison ---")
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print(f"List: {my_list} (mutable - can change)")
my_list[0] = 100
print(f"After change: {my_list}")

print(f"\nTuple: {my_tuple} (immutable - cannot change)")
print("  If you try to change it, you will get an error")


print("\n" + "=" * 60)
print("SECTION 4: PRACTICAL EXERCISE")
print("=" * 60)

#Data
ur_name="Shamaim"
ur_hobby="Sleeping"

#list data
fav_lang=["Java","Python","Js"]
schedule=["Sleep","Eat","Repeat"]

#Tuple data
my_info=("Sky",21,"Fsd")
print(f"name:{ur_name}")
print(f"Hobby:{ur_hobby}")
