"""Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a
product name and print the corresponding price or a message if the product is not in the
dictionary."""

product_dict = {}

print("Enter '0' after entering product's name and values instead of name to exit.\n")

while True:
    name = input("Enter the name of product: ")
    if name == '0':
        break

    try:
        price = float(input(f"Enter price of {name}: "))
        product_dict[name] = price
    except ValueError:
        print("Invalid Value. Please enter a numeric value.")



while True:
    product = input("\nEnter the name of product you want to find (or '0' to exit): ")

    if product == '0':
        break

    if product in product_dict:
        print(f"Price of {product} is: {product_dict[product]}")
    else:
        print(f"{product} is not in the dictionary")