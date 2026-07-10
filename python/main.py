
# Literals
if False:
    # String and Byte Literals #

    # Single/Double Quotes
    print('hello')
    print("world")

    # Triple Quotes
    print("""line one\nline two""")

    # Formatted Strings (f-strings)
    x = 10
    print(f"Value is {x}")

    # Raw Strings (ignore backslash)
    print(r"C:\Users\name")

    # Byte Literals
    print(b"hello")

    # Numeric Literals #
    
    # Integers: 10, -25, 0
    # Digit Grouping: 1_000_000
    # Alternative Bases: 0b101 (binary), 0o755 (octal), 0xFF (hexadecimal)
    # Floating-Point: 3.14, 2.5e-3, (2.5 × 10⁻³ = 0.0025)
    # Complex Numbers: 3 + 4j

    # Boolean and Special Literals #

    # Boolean Truth States: True, False
    # Special Null Literal: None (absence of a value)

# Conditionals
if False:
    name = input("Enter your name: ")
    age = float(input("Enter your age: "))
    greeting = f"Hello, {name}!"

    if age < 13:
        greeting += " Nice to meet you!"
    elif age < 18:
        greeting += " How's it going?"
    elif age < 24:
        greeting += " Welcome, good to see you!"
    else:
        greeting += " Great to have you here!"

    print(greeting)

# Loops
if False:
    # for in : for sequence like (list, string, range)
    for i in range(5):
        print(i)

    for c in "Hello":
        print(c)
    
    fruits = ["apple", "banana", "cherry"] 
    for fruit in fruits:
        print(fruit)

    # while
    i = 0
    while i < 5:
        print(i)
        i += 1

    # Loop control statements: break, continue
    for i in range(10):
        if i == 5:
            break
        print(i)

    for i in range(5):
        if i == 2:
            continue
        print(i)

    # do nothing placeholder
    for i in range(3):
        pass

    # Nested loops
    for i in range(3):
        for j in range(2):
            print(i, j)

# List, Tuple, Set
if False:

    # List: Ordered, Mutable, Allow Duplicates
    nums = [1, 2, 2]
    nums.append(3)     # [1, 2, 2, 3]
    nums[0] = 10       # [10, 2, 2, 3]

    # Tuple: Allow Duplicates, Non Immutable
    t = (1, 2, 2)

    # Set: Unordered, Mutable, No duplicates
    s = {1, 2, 2, 3}   # s is {1, 2, 3}
    s.add(4)           # {1, 2, 3, 4}
    s.remove(2)        # {1, 3, 4}

# Dictionary
if False:
    person = {
        "name": "Ali",
        "age": 22,
        "city": "Lahore"
    }

    val = person["name"]
    val = person.get("country", "Unknown") # Unknown

    val = person["age"] = 23      # update
    val = person["country"] = "Pakistan"  # add

    del person["city"]      # remove key/value
    # person.pop("age")     # remove and return value

    "age" in person                 # True/False
    person.keys()                  # all keys
    person.values()                # all values
    person.items()                 # key-value pairs

# Type casting
if False:
    x = "10"
    y = int(x)   # 10
    x = "3.14"
    y = float(x)  # 3.14
    x = 100
    y = str(x)    # "100"
    x = 0
    bool(x)   # False
    x = 5
    bool(x)   # True
    a = "5"
    b = "2"
    print(int(a) + int(b))   # 7
    # int("abc")  # ValueError
    int(3.99)  # 3

# Exceptions
if False:
    # Basic example
    try:
        x = int("abc")
    except ValueError:
        print("Not a valid integer!")
    
    # Handling multiple exceptions
    try:
        n = int("10")
        d = 10 / 0
    except ValueError:
        print("Bad number format.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

    # Using else (runs if no exception)
    try:
        n = int("10")
    except ValueError:
        print("Bad input.")
    else:
        print("Converted successfully:", n)

    # Using finally (runs always)
    try:
        f = open("file.txt")
    except FileNotFoundError:
        print("File not found.")
    finally:
        print("This runs no matter what.")

# Functions
if False:
    # Define and call
    def greet(name):
        return f"Hello, {name}!"

    msg = greet("Ali")
    print(msg)

    # Without return
    def add(a, b):
        print(a + b)

    add(2, 3)  # prints 5

    # Built-in functions
    """
    Common examples:
        print() → output
        len() → length of a sequence
        type() → type of a value
        int(), float(), str() → type casting
        range() → generates numbers
        sum() → sum of items
        max(), min() → largest/smallest
    """
    nums = [1, 2, 3, 4]
    print(len(nums))        # 4
    print(sum(nums))        # 10
    print(max(nums))        # 4

# Type annotations
if False:
    # with function
    def add(a: int, b: int) -> int:
        return a + b
    
    num = add(2, 3)
    
    # with variables
    name: str = "Ali"
    age: int = 22

    # Common built-ins
    from typing import List
    nums: List[int] = [1, 2, 3]

# Basic Math
if False:
    score = 0
    health = 0
    score = score + 50      # Addition (score is now 50)
    health = health - 10.5  # Subtraction (health is now 90.0)
    damage = 5 * 2          # Multiplication (damage is 10)
    power = 3 ** 2          # Exponent (3 to the power of 2 = 9)

    # F String
    name = "Alex"
    item = "Health Potion"
    quantity = 3
    price = 15.50
    total_cost = quantity * price
    receipt = f"Thanks {name}! {quantity}x {item} costs ${total_cost:.2f}."
    print(receipt)

# Scopes
# Classes
# Modules
# Lambda Functions
# Map, Filter, Reduce
# Decorators

# List Compression
if True:
    numbers = [1, 2, 3, 4, 5]

    numbers_power_2 = [n**2 for n in numbers]
    print(numbers_power_2)

# Operator overloading













    

