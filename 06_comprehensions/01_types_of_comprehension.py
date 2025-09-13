# List Comprehension
# Syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
print("List Comprehension (squares):", squares)

# Dictionary Comprehension
# Syntax: {key_expression: value_expression for item in iterable if condition}
square_dict = {x: x**2 for x in range(10)}
print("Dictionary Comprehension (squares):", square_dict)

# Set Comprehension
# Syntax: {expression for item in iterable if condition}
unique_squares = {x**2 for x in range(-3, 4)}
print("Set Comprehension (unique squares):", unique_squares)

# Generator Comprehension
# Syntax: (expression for item in iterable if condition)
square_gen = (x**2 for x in range(5))
print("Generator Comprehension (first 5 squares):", list(square_gen))

# You can use comprehensions to filter as well:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("List Comprehension with condition (even squares):", even_squares)
