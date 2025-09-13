# Function with various types of parameters
def my_function(a, b, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

print("--- Calling with positional and keyword arguments ---")
my_function(1, 2, "hello", "world", name="Ayush", age=24)

print("\n--- Calling with only positional arguments ---")
my_function(1, 2, 3, 4, 5)

print("\n--- Calling with only keyword arguments ---")
my_function(a=1, b=2, city="New York", country="USA") #what ever in key-value pair is kwargs and rest is args 
# single * is for args and double ** is for kwargs , *args is for multiple values in tuple and **kwargs is for multiple key-value pairs


def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)


make_chai("Ginger","yes","low")#positional arguments
make_chai(milk="yes",sugar="low",tea="Ginger")#keyword arguments
make_chai("Ginger",sugar="low",milk="yes")#both positional and keyword arguments
#positional arguments should always be before keyword arguments


def special_chai(*ingredients,**extras):
    print(ingredients)#tuple means args
    print(extras)#dictionary means kwargs
special_chai("Ginger","Elaichi","Tulsi",milk="yes",sugar="low",honey="yes")