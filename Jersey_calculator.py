price = float(input("Enter jersey price: $"))
tax_rate = 0.06625
tax = price * tax_rate
total_price = price + tax
print("Tax: $", round(tax, 2))
print("Total Price: $", round(total_price, 2))