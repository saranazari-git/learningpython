"""
==================================================
File: conditionals.py
Description: Learn how to use if, elif, and else statements in Python
==================================================
"""

# ==================================================
# 1. BASIC IF STATEMENT
# ==================================================
# The code inside the 'if' block runs only if the condition is True.
age = 20

print("--- 1. Basic If Statement ---")
if age >= 18:
    print("You are an adult.")


# ==================================================
# 2. IF-ELSE STATEMENT
# ==================================================
# If the condition is True, the 'if' block runs. Otherwise, the 'else' block runs.
temperature = 28

print("\n--- 2. If-Else Statement ---")
if temperature > 30:
    print("It's a hot day outside! ☀️")
else:
    print("The weather is pleasant. 🌤️")


# ==================================================
# 3. IF-ELIF-ELSE STATEMENT (Multiple Conditions)
# ==================================================
# Used when you have multiple conditions to check sequentially.
score = 85

print("\n--- 3. If-Elif-Else Statement ---")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Your score is {score}, so your grade is: {grade}")


# ==================================================
# 4. LOGICAL OPERATORS (and, or, not)
# ==================================================
# You can combine multiple conditions using logical operators.
has_id = True
is_student = False

print("\n--- 4. Logical Operators ---")
# 'and': Both conditions must be True
if has_id and is_student:
    print("Access granted with student discount.")
# 'or': At least one condition must be True
elif has_id or is_student:
    print("Access granted standard entry.")
else:
    print("Access denied.")


# ==================================================
# 5. NESTED IF STATEMENTS
# ==================================================
# An if statement inside another if statement.
is_logged_in = True
is_admin = True

print("\n--- 5. Nested If Statements ---")
if is_logged_in:
    if is_admin:
        print("Welcome, Admin! Full access granted.")
    else:
        print("Welcome, User! Limited access granted.")
else:
    print("Please log in first.")
