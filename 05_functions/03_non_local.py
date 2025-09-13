# Demonstrating local and nonlocal variable scopes
def update_order():
    chai_type = "Elaichi" # Local variable
    print(f"Chai type outside the kitchen: {chai_type}")
    def kitchen():
        nonlocal chai_type  # when we want to access the variable from the outer function in inside the function
        chai_type = "kesar"
        print(f"Chai type in kitchen: {chai_type}")
    kitchen()
    
    print(f"Chai type in update_order: {chai_type}")

update_order()
# Output:
# Chai type outside the kitchen: Elaichi
# Chai type in kitchen: kesar
# Chai type in update_order: kesar
