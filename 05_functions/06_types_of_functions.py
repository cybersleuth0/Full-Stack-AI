# Pure Function Example
def add(a, b):
    """This is a pure function. It always returns the same output for the same inputs and has no side effects."""
    return a + b

# Impure Function Example
external_list = []

def add_to_list(item):
    """This is an impure function. It modifies an external variable (side effect)."""
    external_list.append(item)
    return external_list

# Usage examples:
print("Pure function output:", add(2, 3))  # Always 5

print("Impure function output:", add_to_list(10))  # Modifies external_list
print("Impure function output:", add_to_list(20))  # Modifies external_list again

# Summary:
# Pure functions:
#   - Output depends only on input
#   - No side effects (do not modify external state)
# Impure functions:
#   - May have side effects (modify external state, print, read/write files, etc.)
#   - Output can depend on or change something outside the function



# Lambda Function Example:
# A lambda function is a small anonymous function defined with the lambda keyword.

# Syntax: lambda arguments: expression
# For example:
# lambda x, y: x + y
# This creates a function that takes two arguments and returns their sum.
# Example:
double = lambda x: x * 2
print("Lambda function output (double 5):", double(5))  # Output: 10

chai_types=["Elaichi","Ginger","Tulsi","Masala","Ginger"]
# Using lambda with filter to find all "Ginger" chai types
strong_chai=list(filter(lambda x: x=="Ginger", chai_types))
print(strong_chai)
strong_chai=list(filter(lambda x: x!="Ginger", chai_types))
print(strong_chai)