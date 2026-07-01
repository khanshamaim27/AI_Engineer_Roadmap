# AI Engineer 3-Month Roadmap
## Progress Tracker

### Month 1: Foundation
- [ ] Week 1: Python Basics
- [ ] Week 2: Advanced Python
- [ ] Week 3: Math for AI
- [ ] Week 4: ML Intro

### Month 2: Machine Learning
- [ ] Week 5: Classification
- [ ] Week 6: Unsupervised Learning
- [ ] Week 7: Deep Learning Intro
- [ ] Week 8: Advanced Deep Learning

### Month 3: Portfolio + Interview
- [ ] Week 9: Project 1 (House Price Prediction)
- [ ] Week 10: Project 2 (Sentiment Analysis)
- [ ] Week 11: Project 3 (Image Classification)
- [ ] Week 12: Interview Prep

### 
- Started Python basics
- Completed: Variables, Data Types
- Time spent: 1.5 hrs

#Ditionaries-Day-4

# ============================
# PYTHON DICTIONARIES
# ============================

# A dictionary is a collection of information.

# A dictionary stores data in KEY : VALUE pairs.

# Think of a real dictionary.
# Word -> Meaning

# Example:
# Apple -> A fruit
# Cat -> An animal

# In Python:
# Key -> Value

# Example:
# "name" -> "Musa"
# "age" -> 18
# "city" -> "Lahore"

# Dictionaries use curly braces {}

student = {
    "name": "Shamaim khan"
    "age": 21,
    "city": "Faisalabad"
}

# ----------------------------
# KEY and VALUE
# ----------------------------

# "name" is the KEY
# "Musa" is the VALUE
# "age" is the KEY
# 18 is the VALUE
# "city" is the KEY
# "Lahore" is the VALUE

# ----------------------------
# WHY USE A DICTIONARY?
# ----------------------------

# Lists use index numbers.

fruits = ["Apple", "Banana", "Orange"]

# Apple = index 0
# Banana = index 1
# Orange = index 2

# Dictionaries use names (keys) instead of indexes.

student = {
    "name": "Musa",
    "age": 18
}

# Instead of remembering index numbers,
# we use the key.

# student["name"] gives "Musa"
# student["age"] gives 18


# ----------------------------
# KEYS
# ----------------------------

# Keys must be UNIQUE.
# Two keys cannot have the same name.

# Wrong

student = {
    "name": "Ali",
    "name": "Ahmed"
}

# Python will keep only one "name" key.


# ----------------------------
# VALUES
# ----------------------------

# Values CAN be repeated.

student = {
    "student1": "Ali",
    "student2": "Ali"
}

# This is completely fine.


# ----------------------------
# ACCESSING A VALUE
# ----------------------------

student = {
    "name": "Musa",
    "age": 18
}

# Use square brackets with the key.

# student["name"] -> "Musa"
# student["age"] -> 18


# ----------------------------
# UPDATING A VALUE
# ----------------------------

student["age"] = 19

# Age changes from 18 to 19.


# ----------------------------
# ADDING A NEW KEY
# ----------------------------

student["city"] = "Lahore"

# Dictionary now has a new key called "city".


# ----------------------------
# REMEMBER
# ----------------------------

# List = [] = Uses indexes (0,1,2...)

# Tuple = () = Cannot be changed

# Dictionary = {} = Uses KEY : VALUE pairs