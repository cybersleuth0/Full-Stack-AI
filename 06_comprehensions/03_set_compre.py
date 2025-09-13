favorite_chai = [
    "masala chai",
    "green chai",
    "ginger chai",
    "herbal chai",
    "Elaichi chai",
    "masala chai",
    "green chai"
]
unique_chai = {chai for chai in favorite_chai if len(chai) > 9}
print("Unique types of chai:", unique_chai)# Set Comprehension
# Syntax: {expression for item in iterable if condition}
# Set comprehension syntax:
#   {expression for item in iterable if condition}
# - 'expression' is what you want in the new set (can be 'item' or a transformation of it)
# - 'iterable' is the source collection (like 'favorite_chai')
# - 'condition' is optional; filters which items are included
#
# Example: Get all unique chai names longer than 9 characters
#   {chai for chai in favorite_chai if len(chai) > 9}

recipes = {
    "masala chai": ["water", "milk", "tea leaves", "spices", "sugar"],
    "green chai": ["water", "milk", "green tea leaves", "sugar"],
    "ginger chai": ["water", "milk", "tea leaves", "ginger", "sugar"],
    "herbal chai": ["water", "milk", "herbal tea leaves", "honey"],
    "Elaichi chai": ["water", "milk", "tea leaves", "cardamom", "sugar"]
}
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print("Unique spices used:", unique_spices)

# Example: Set comprehension to find all unique vowels in chai names
vowels = {'a', 'e', 'i', 'o', 'u'}
unique_vowels_in_chai = {char for name in recipes.keys() for char in name if char in vowels}
print("Unique vowels in chai names:", unique_vowels_in_chai)