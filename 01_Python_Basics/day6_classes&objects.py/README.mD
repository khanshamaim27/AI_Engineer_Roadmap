# 🌍 Day 6 - Planet Class (Python OOP)

## 📚 Objective

This project is part of my **Python Learning Journey**.

The goal was to practice:

- Creating classes
- Creating objects
- Using constructors (`__init__`)
- Instance attributes
- Methods
- Special methods (`__str__`)
- Exception handling (`TypeError` and `ValueError`)

---

# 🧠 What You'll Learn

After completing this project you should understand:

- What a class is
- What an object is
- How `self` works
- How constructors initialize objects
- How to validate user input
- How to create your own methods
- How `__str__()` changes object printing

---

# 📖 Project Overview

We create a `Planet` class that stores:

- Planet Name
- Planet Type
- Star

Example:

```
Planet: Earth | Type: Terrestrial | Star: Sun
```

Each planet can also orbit its star.

Example:

```
Earth is orbiting around Sun....
```

---

# 🛠 Concepts Used

## 1. Constructor

```python
def __init__(self, name, planet_type, star):
```

The constructor runs automatically whenever a new object is created.

Example:

```python
planet_1 = Planet("Earth", "Terrestrial", "Sun")
```

---

## 2. self

`self` refers to the current object.

Example:

```python
self.name = name
```

This stores the value inside the object.

Without `self`, Python wouldn't know which object's data you're referring to.

---

## 3. Input Validation

Before saving values, we check if they are valid.

### Type Checking

```python
if type(name) != str:
```

Raises

```python
TypeError
```

if the user enters something other than a string.

Example:

```python
Planet(123, "Gas Giant", "Sun")
```

---

### Empty String Checking

```python
if name == "":
```

Raises

```python
ValueError
```

Example:

```python
Planet("", "Gas Giant", "Sun")
```

---

## 4. Instance Attributes

```python
self.name = name
self.planet_type = planet_type
self.star = star
```

These variables belong to each object individually.

Example:

```
planet_1.name
planet_2.name
```

can store different values.

---

## 5. Methods

Methods are functions inside a class.

Example:

```python
def orbit(self):
```

Methods describe what an object can do.

---

## 6. __str__()

`__str__()` is a special Python method.

Whenever you do

```python
print(planet_1)
```

Python automatically calls

```python
planet_1.__str__()
```

Without it, Python prints something like:

```
<__main__.Planet object at 0x0000024A...>
```

With it, we get a readable output.

---

# Common Beginner Mistakes

### ❌ Forgetting `self`

Wrong

```python
return f"{name}"
```

Correct

```python
return f"{self.name}"
```

---

### ❌ Using `print()` instead of `return`

Wrong

```python
print("Earth is orbiting...")
```

Correct

```python
return "Earth is orbiting..."
```

---

### ❌ Writing methods inside `__init__`

Wrong

```python
class Planet:

    def __init__(...):

        def orbit():
```

Correct

```python
class Planet:

    def __init__(...):
        ...

    def orbit():
```

Notice both methods have the same indentation.

---

### ❌ Using `=` instead of `==`

Wrong

```python
if name = "":
```

Correct

```python
if name == "":
```

---

### ❌ Forgetting the colon

Wrong

```python
def orbit(self)
```

Correct

```python
def orbit(self):
```

---

# Output

```
Planet: Earth | Type: Terrestrial | Star: Sun
Planet: Jupiter | Type: Gas Giant | Star: Sun
Planet: Mars | Type: Terrestrial | Star: Sun

Earth is orbiting around Sun....
Jupiter is orbiting around Sun....
Mars is orbiting around Sun....
```

---

# Skills Practiced

- Classes
- Objects
- Constructors
- Instance Attributes
- Methods
- Special Methods
- Exception Handling
- Object Creation
- Python OOP Basics

---

# What I Learned

This project helped me understand the difference between:

- Class vs Object
- Attribute vs Method
- `print()` vs `return`
- `=` vs `==`
- `self.variable` vs local variables
- Regular methods vs Special methods (`__str__`)

---

⭐ Day 6 Complete!