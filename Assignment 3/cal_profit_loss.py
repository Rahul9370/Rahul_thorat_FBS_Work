# 6. Write a program to calculate profit or loss.

cost_price = int(input("Enter a Cost Price :"))
selling_price = int(input("Enter a Selling Price :" ))

profit = selling_price - cost_price
loss = cost_price - selling_price

if(cost_price < selling_price):
    print("You got Profit of Rs.",profit)
else:
    print("You got loss of Rs.",loss)