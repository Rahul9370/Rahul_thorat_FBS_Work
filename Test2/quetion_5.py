# A man goes for shopping and buys 5 products. He needs to calculate the total bill amount including 18% GST.

product_1 = int(input("Enter the price of product 1: "))
product_2 = int(input("Enter the price of product 2: "))
product_3 = int(input("Enter the price of product 3: "))
product_4 = int(input("Enter the price of product 4: "))
product_5 = int(input("Enter the price of product 5: "))

total_bill = (product_1 + product_2 + product_3 + product_4 + product_5) * 1.18  # Adding 18% GST

print("Total bill amount is: ", total_bill)
