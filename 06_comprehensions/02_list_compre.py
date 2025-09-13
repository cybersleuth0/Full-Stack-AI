menu = [
    "Masala Chai",
    "Iced Coffee",
    "Iced Juice",
    "Lemonade"
    ]

# NOTE:
# List comprehension syntax:
#   [expression for item in iterable if condition]
# - 'expression' is what you want in the new list (can be 'item' or a transformation of it)
# - 'iterable' is the source collection (like 'menu')
# - 'condition' is optional; filters which items are included

# Example: Get all items in menu that contain "Iced"
iced_drinks=[item for item in menu if "Iced" in item ]
print(iced_drinks)


