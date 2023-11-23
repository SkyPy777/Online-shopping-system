# Simple Python Online Shopping System

# user input for total purchase amount
total_amount = float(input("\nEnter the total purchase amount: "))

# Apply discounts based on the total amount
if total_amount >= 100:
    discount = 20
elif total_amount >= 50:
    discount = 10
else:
    discount = 5

# Calculate the discounted amount
discounted_amount = total_amount - (total_amount * discount / 100)

# Display the receipt
print("\n===== Receipt =====")
print(f"Total Amount: ${total_amount:.2f}")
print(f"Discount: {discount}%")
print(f"Discounted Amount: ${discounted_amount:.2f}")
print("===================")

# Check if the user wants to proceed with the purchase
proceed = input("\nDo you want to proceed with the purchase? (yes/no): ")

# Display user's decision
if proceed.lower() == 'yes':
    print("\nThank you for your purchase! Your order has been placed.")
else:
    print("\nNo problem. Visit again.")

