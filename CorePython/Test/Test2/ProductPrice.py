# A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

p1=int(input("Enter first product price:"))
p2=int(input("Enter second product price:"))
p3=int(input("Enter third product price:"))
p4=int(input("Enter fourth product price:"))
p5=int(input("Enter fifth product price:"))



price=p1+p2+p3+p4+p5

gst=0.18

gst_price=price*gst

total_price=price+gst_price

print(f'Total bill of products with 18% gst is {total_price} Rs')


