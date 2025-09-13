# Demonstrating global variable scope
chai_type = "Elaichi"  # Global variable
print(f"Chai type outside the function: {chai_type}")

def update_order():
    global chai_type # we can access and modify the global variable inside the function
    chai_type = "kesar"
    print(f"Chai type in update_order: {chai_type}")

update_order()
print(f"Chai type outside the function: {chai_type}")
