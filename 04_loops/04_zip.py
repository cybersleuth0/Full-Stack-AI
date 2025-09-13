names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# zip combines elements from multiple iterables (like lists) into tuples.


combined = list(zip(names, ages))
print(combined)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

# Example with lists of different lengths:
cities = ["New York", "London"]
# Only two pairs will be created, as 'cities' has only two elements.
print(list(zip(names, ages, cities)))  # Output: [('Alice', 25, 'New York'), ('Bob', 30, 'London')]