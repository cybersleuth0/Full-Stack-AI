# Your task is to create a list of squares of all even numbers from 1 to 20.
# You must use a list comprehension to solve this.

# For example, the first few numbers in your list should be:
# 2*2 = 4
# 4*4 = 16
# 6*6 = 36
# ... and so on.

# Write your code below this line:
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(even_squares)