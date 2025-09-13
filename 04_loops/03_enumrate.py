menu=["Home", "About", "Contact"]
print(list(enumerate(menu)))
for index, item in enumerate(menu,start=2):
    print(f"Item {index}: {item}")