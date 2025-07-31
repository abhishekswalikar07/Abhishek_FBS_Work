# WAP to calculate selling price of book based on cost price and discount.

CP=float(input("Enter cost price of book:"))
Dis=float(input("Enter discount price of book:"))

SP=CP+Dis
# SP=SP+CP
print(f'Selling price of book is {SP}.')


# 2


cost_price = float(input("Enter the cost price of the book: ₹"))
discount = float(input("Enter the discount percentage: "))


discount_amount = (discount / 100) * cost_price


selling_price = cost_price + discount_amount


print(f"Selling price of the book: ₹{selling_price}")
