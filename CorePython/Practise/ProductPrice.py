# Find the price of item when discount is given(Speciffy differnt discount based on prices)

price=int(input("Enter total price of items:"))

dis=0

if price<=500:
    dis=price*0.05
    total_price=price-dis
elif 500 <price <=1000:
    dis=price*0.1
    total_price=price-dis
elif 1000 <price <=1500:
    dis=price*0.15
    total_price=price-dis
elif 1500 <price <=2000:
    dis=price*0.2
    total_price=price-dis
elif 2000 <price <=2500:
    dis=price*0.25
    total_price=price-dis
else:
    print("Enter correct price.")
    
print(f"Total price of items is {total_price}")