# Example of the walrus operator (:=)

# Without walrus operator
# hot_tea = 10
# while hot_tea > 0:
#     print(f"Remaining hot tea: {hot_tea}")
#     hot_tea -= 1

# With walrus operator
print("\n--- Walrus Operator Example ---")
hot_tea = 10
while (hot_tea := hot_tea - 1) >= 0:
    print(f"Remaining hot tea: {hot_tea + 1}") # +1 because hot_tea is already decremented

# Another example: assigning a value and checking it in an if statement
print("\n--- Walrus Operator in if statement ---")
if (length := len("Chai aur code")) > 10:
    print(f"The string is too long ({length} characters).")

# Example in a list comprehension
print("\n--- Walrus Operator in List Comprehension ---")
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_data = [y for x in data if (y := x * 2) > 10]
print(f"Filtered data (doubled values > 10): {filtered_data}")




# Note: The walrus operator is available in Python 3.8 and later versions.
available_sizes = ["S", "M", "L", "XL"]
if (requested_size := input("What size do you want? ")) in available_sizes:
    print(f"Size {requested_size} is available.")
else:
    print(f"Size {requested_size} is not available.")
    