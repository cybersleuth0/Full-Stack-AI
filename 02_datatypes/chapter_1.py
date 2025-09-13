# how_many_items_A = 5
# how_many_items_b = 10

# print(f"Id of 5 is: {id(5)}")
# print(f"Id of 10 is:{id(10)}")

# Immutable types: int, float, str, tuple, frozenset, bool, bytes

immutable_examples = [5, 3.14, "hello", (1, 2), frozenset([1, 2]), True, b'abc']

# Mutable types: list, dict, set, bytearray
mutable_examples = [[1, 2], {"a": 1}, {1, 2}, bytearray(b'abc')]

print("Immutable types and their ids:")
for item in immutable_examples:
    print(f"Type: {type(item).__name__}, Value: {item}, Id: {id(item)}")

print("\nMutable types and their ids:")
for item in mutable_examples:
    print(f"Type: {type(item).__name__}, Value: {item}, Id: {id(item)}")


