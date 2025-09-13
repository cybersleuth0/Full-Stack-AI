# basic of list

ingredients = ["egg", "milk", "butter", "flour", "sugar"]
ingredients.append("salt")# add item to the end of list
ingredients.remove("milk")# remove item from list
ingredients[2] = "whole wheat flour"# modify item in list
print(ingredients)

# add two lists
more_ingredients = ["baking powder", "vanilla extract"]

# all_ingredients = ingredients + more_ingredients
all_ingredients = ingredients.extend(more_ingredients)

ingredients.insert(1, "honey")# insert item at specific index
print(ingredients)

last_item = ingredients.pop()# remove and return last item
print(f"Removed item: {last_item}")
print(ingredients)

print(f"Number of ingredients: {len(ingredients)}")# length of list
# The general slice syntax is [start:stop:step].
# Leaving start and stop empty means "from the beginning to the end".
# The -1 as the step means "move backwards", so it reverses the order.
print(f"Reversed ingredients: {ingredients[::-1]}")# reversed list
ingredients.reverse()
print(f"Reversed ingredients using reverse(): {ingredients}")# reverse list