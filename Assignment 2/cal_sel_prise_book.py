# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input("         Enter cost price of book:"))
discount = int(input("Enter discount percentage on book:"))

selling_price = cost_price - (discount * cost_price / 100)

print("       Selling price of Book is:",selling_price)