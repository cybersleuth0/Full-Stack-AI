# This creates a dictionary where the keys are numbers from 0 to 4,
# and the values are the squares of those numbers.
squares = {x: x**2 for x in range(5)}
print("Squares:", squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Dictionary comprehension with condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print("Even Squares:", even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swapping keys and values in a dictionary
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print("Swapped:", swapped)  # {1: 'a', 2: 'b', 3: 'c'}

# Using dict comprehension to filter items
filtered = {k: v for k, v in original.items() if v > 1}
print("Filtered:", filtered)  # {'b': 2, 'c': 3}

# Nested dict comprehension
matrix = [[1, 2], [3, 4]]
flattened = {(i, j): matrix[i][j] for i in range(2) for j in range(2)}
print("Flattened matrix:", flattened)  # {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4}

# Explanation:
# {key_expr: value_expr for item in iterable if condition}
# - key_expr: expression for the key
# - value_expr: expression for the value
# - iterable: any iterable (like list, range, dict.items())
# - condition: (optional) filter for which items to include
