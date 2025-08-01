CP=int(input("Enter cost price of product."))
SP=int(input("Enter cost price of product."))

if SP> CP:
    print("Profit")
elif CP>SP:
    print("Loss")
else:
    print("No profit nor loss")