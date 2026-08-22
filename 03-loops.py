"""
==================================================
File: loops.py
Description: Learn how to use for and while loops in Python
==================================================
"""

# ==================================================
# 1. FOR LOOP (Iterating over a sequence)
# ==================================================
# A 'for' loop is used for iterating over a sequence (like a list, tuple, string, or range).

print("--- 1. Basic For Loop with Range ---")
# range(5) generates numbers from 0 up to 4
for i in range(5):
    print(f"Current number: {i}")


print("\n--- 2. For Loop through a List ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")


print("\n--- 3. For Loop through a String ---")
for letter in "Python":
    print(letter)


# ==================================================
# 4. WHILE LOOP
# ==================================================
# A 'while' loop executes as long as a condition remains True.

print("\n--- 4. Basic While Loop ---")
count = 1
while count <= 3:
    print(f"Count is: {count}")
    count += 1  # Increment count to avoid an infinite loop!


# ==================================================
# 5. LOOP CONTROL STATEMENTS (break and continue)
# ==================================================

print("\n--- 5. Break Statement ---")
# 'break' stops the loop entirely even if the condition is still true.
for num in range(1, 10):
    if num == 5:
        print("Reached 5, stopping the loop.")
        break
    print(num)


print("\n--- 6. Continue Statement ---")
# 'continue' skips the current iteration and moves to the next one.
for num in range(1, 6):
    if num == 3:
        print("Skipping number 3.")
        continue
    print(f"Processing number: {num}")
