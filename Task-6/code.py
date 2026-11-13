print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

total_bill = 0

# Processing multiple products
for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (Food/Electronics/Clothing): ").lower()

    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Calculate subtotal
    subtotal = price * quantity

    # Calculate category-specific tax
    if category == "food":
        tax_rate = 0.05

    elif category == "electronics":
        tax_rate = 0.18

    elif category == "clothing":
        tax_rate = 0.12

    else:
        print("Invalid category!")
        continue

    tax = subtotal * tax_rate

    # Calculate discount
    if subtotal >= 5000:
        discount = subtotal * 0.15

    elif subtotal >= 2000:
        discount = subtotal * 0.10

    else:
        discount = subtotal * 0.05

    # Apply maximum discount limit
    discount = min(discount, 1000)

    # Calculate final amount
    final_amount = subtotal + tax - discount

    total_bill = total_bill + final_amount

    # Display product details
    print("\nProduct Name:", name)
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Tax: Rs.", round(tax, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Final Amount: Rs.", round(final_amount, 2))

# Display final invoice
print("\n========== FINAL INVOICE ==========")
print("Total Bill Amount: Rs.", round(total_bill, 2))
print("===================================")
