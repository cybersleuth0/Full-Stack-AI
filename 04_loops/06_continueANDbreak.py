# Example of 'break' statement
print("--- Break Example ---")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("Current value (break):", i)

# Example of 'continue' statement
print("\n--- Continue Example ---")
for i in range(1, 10):
    if i % 2 == 0:  # Skip even numbers
        print("Skipping even number:", i)
        continue
    print("Current value (continue):", i)
