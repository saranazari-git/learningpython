"""
==================================================
File: main.py
Description: Comprehensive guide to Python Variables and Data Types
==================================================
"""

# ==================================================
# 1. WHAT IS A VARIABLE?
# ==================================================
# A variable is a container for storing data values. 
# You don't need to explicitly declare the data type; Python figures it out automatically.
x = 10         # x is an integer
name = "Sara"  # name is a string

print("--- 1. Basic Variables ---")
print("x =", x)
print("name =", name)


# ==================================================
# 2. NUMERIC DATA TYPES
# ==================================================
# Integers (int): Whole numbers
age = 30

# Floats (float): Numbers with decimals
temperature = 36.6

# Complex numbers (complex): Numbers with a real and imaginary part
complex_num = 2 + 3j

print("\n--- 2. Numeric Types ---")
print(f"Age: {age} (Type: {type(age)})")
print(f"Temperature: {temperature} (Type: {type(temperature)})")


# ==================================================
# 3. TEXT DATA TYPE (STRING)
# ==================================================
# Strings (str) are surrounded by either single or double quotation marks.
first_name = "Python"
last_name = 'Developer'

# String concatenation (combining strings)
full_name = first_name + " " + last_name

# F-strings (formatted string literals) - Best practice for injecting variables
greeting = f"Hello, my name is {full_name} and I am {age} years old."

print("\n--- 3. String Type ---")
print(greeting)
print(f"Length of full name: {len(full_name)}")


# ==================================================
# 4. BOOLEAN DATA TYPE
# ==================================================
# Booleans (bool) represent one of two values: True or False.
is_learning = True
is_difficult = False

print("\n--- 4. Boolean Type ---")
print("Is learning Python?", is_learning)
print("Result of 5 > 10:", 5 > 10)  # Evaluates to False


# ==================================================
# 5. SEQUENCE DATA TYPES (Lists, Tuples, Ranges)
# ==================================================

# A. List: Ordered, changeable (mutable), allows duplicate members. Uses square brackets [].
languages = ["Python", "Java", "C++", "Python"]

# B. Tuple: Ordered, unchangeable (immutable), allows duplicate members. Uses parentheses ().
coordinates = (10.5, 20.3)

# C. Range: Represents a sequence of numbers (often used in loops).
number_range = range(6)  # 0 to 5

print("\n--- 5. Sequence Types ---")
print("Languages List:", languages)
print("First language:", languages[0])  # Indexing starts at 0
print("Coordinates Tuple:", coordinates)


# ==================================================
# 6. MAPPING DATA TYPE (Dictionary)
# ==================================================
# Dictionary (dict): Unordered, changeable, and indexed. Uses key-value pairs {}.
user_profile = {
    "username": "saranazari",
    "field": "Computer Engineering",
    "active_status": True
}

print("\n--- 6. Dictionary Type ---")
print("User Profile:", user_profile)
print("User's field:", user_profile["field"])


# ==================================================
# 7. SET DATA TYPES (Set, Frozenset)
# ==================================================
# Set: Unordered, unindexed, no duplicate values allowed. Uses curly braces {}.
unique_numbers = {1, 2, 3, 3, 2, 1}

print("\n--- 7. Set Type ---")
print("Unique numbers (duplicates removed):", unique_numbers)


# ==================================================
# 8. TYPE CASTING (Converting between types)
# ==================================================
# You can convert data types explicitly using constructor functions like int(), str(), float(), etc.
num_str = "123"
num_int = int(num_str)  # Converts string "123" to integer 123

print("\n--- 8. Type Casting ---")
print(f"Original string: '{num_str}' (Type: {type(num_str)})")
print(f"Converted integer: {num_int} (Type: {type(num_int)})")
print(f"Math check (num_int + 7): {num_int + 7}")
