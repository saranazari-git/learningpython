"""
==================================================
File: functions.py
Description: Learn how to define and use functions, parameters, and return values in Python
==================================================
"""

# ==================================================
# 1. DEFINING AND CALLING A BASIC FUNCTION
# ==================================================
# Use the 'def' keyword to define a function.
def say_hello():
    print("Hello! Welcome to Python functions.")

print("--- 1. Basic Function ---")
# Calling the function
say_hello()


# ==================================================
# 2. FUNCTIONS WITH PARAMETERS AND ARGUMENTS
# ==================================================
# You can pass data (parameters) into a function.
def greet_user(name):
    print(f"Hello, {name}! Good to see you.")

print("\n--- 2. Function with Parameters ---")
greet_user("Sara")
greet_user("Ali")


# ==================================================
# 3. RETURN VALUES
# ==================================================
# Functions can return a result back using the 'return' keyword.
def add_numbers(a, b):
    return a + b

print("\n--- 3. Function with Return Value ---")
result = add_numbers(5, 7)
print(f"The sum is: {result}")


# ==================================================
# 4. DEFAULT PARAMETER VALUES
# ==================================================
# You can assign a default value to a parameter if no argument is provided.
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

print("\n--- 4. Default Parameters ---")
describe_pet("Whiskers", "cat")  # Uses provided animal_type
describe_pet("Max")             # Uses default animal_type ("dog")


# ==================================================
# 5. LAMBDA FUNCTIONS (Anonymous Functions)
# ==================================================
# A lambda function is a small anonymous function defined with the 'lambda' keyword.
# Syntax: lambda arguments : expression

print("\n--- 5. Lambda Functions ---")
square = lambda x: x * x
print(f"Square of 4 is: {square(4)}")
