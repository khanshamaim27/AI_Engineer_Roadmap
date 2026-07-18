# Day 7— OOP Basics 


## 1. Classes & Objects

A **class** is a blueprint. An **object** is one real thing built from that blueprint.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car('Toyota', 'red')
print(car1.brand)  # Toyota
```

**`self`** = "this specific object." It lets each object keep its own separate data, even though they all come from the same class.

---

## 2. Encapsulation — Hiding Data

Bundle data + actions together in a class, and hide the raw data behind safe methods — like a TV remote: you press buttons, you don't touch the wires inside.

```python
class Wallet:
    def __init__(self, balance):
        self.__balance = balance   # hidden

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

- `_balance` (1 underscore) → "please don't touch" (just a polite rule, not enforced)
- `__balance` (2 underscores) → actually blocked from outside access

**Why it matters:** stops people from setting bad data directly, like `balance = -9999`. All changes must go through safe, checked methods.

---

## 3. Getters, Setters & Properties — Clean Access to Hidden Data

A **property** lets a method be used like a plain attribute (no `()` needed), while still running logic behind the scenes.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius   # goes through the setter

    @property
    def radius(self):              # getter — reads the value
        return self._radius

    @radius.setter
    def radius(self, value):       # setter — checks before saving
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
```

- **Getter** (`@property`) → runs when you *read* `obj.radius`
- **Setter** (`@radius.setter`) → runs when you *assign* `obj.radius = value`, and can validate first
- **Deleter** (`@radius.deleter`) → runs when you do `del obj.radius`

⚠️ **Watch out:** inside getter/setter, always use `self._radius` (underscore), never `self.radius` — otherwise it calls itself forever and crashes (`RecursionError`).

---

## 4. Inheritance — Reusing Code

A **child class** can reuse everything from a **parent class**, without rewriting it.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):        # Dog inherits from Animal
    bark = 'woof!'

jack = Dog('Jack')
print(jack.sound())   # Jack makes a sound (reused from Animal)
```

- **Override** → child rewrites a method completely, replacing the parent's version.
- **Extend** → child keeps the parent's behavior and adds more, using `super()`:

```python
def sound(self):
    base = super().sound()          # run parent's version first
    return f'{base}, then barks {self.bark}'
```

- **Multiple inheritance** → a class can inherit from more than one parent:
```python
class Amphibian(Walker, Swimmer):
    pass
```

---

## 5. Abstraction — Show Only What's Needed

Hide complicated internal logic, expose only the essential parts. Like driving a car: you use the steering wheel and pedals, you don't need to know how the engine works.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Woof!')
```

- `ABC` → a class meant only to be inherited from — you can't create an object directly from it.
- `@abstractmethod` → forces every subclass to provide its own version of that method.
- If a subclass forgets to implement it, Python blocks you from creating that object (`TypeError`).

---

## Encapsulation vs Abstraction (easy to confuse)

| | Hides what | Purpose |
|---|---|---|
| **Encapsulation** | Data (`__balance`) | Protects data from bad/unsafe changes |
| **Abstraction** | Complexity | Keeps things simple to use |

---

## The 4 Pillars of OOP — Quick Recap

1. **Encapsulation** → hide data, expose safe methods
2. **Inheritance** → reuse code from a parent class
3. **Polymorphism** → same method name, different behavior per class *(covered separately)*
4. **Abstraction** → hide complexity, show only essentials

---

## Underscore Cheat Sheet

| Prefix | Meaning |
|---|---|
| `_name` | Convention — "internal use, don't touch" (not enforced) |
| `__name` | Enforced — Python blocks direct outside access (name mangling) |

---

## Key One-Liners to Remember

- `self` = the specific object currently being worked on.
- `__init__` sets up an object's data the moment it's created.
- Properties = methods that act like attributes.
- `super()` = "run the parent's version of this first."
- `ABC` + `@abstractmethod` = "this method is required, but I won't say how."