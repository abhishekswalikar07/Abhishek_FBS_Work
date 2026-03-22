try:
    bill = float(input("Enter bill amount: "))
    if bill < 0:
        raise ValueError("Bill amount cannot be negative.")
    dis = 0
    if bill < 1000:
        dis = bill * 0.05
    elif 1000 <= bill <= 5000:
        dis = bill * 0.1
    else:
        dis = bill * 0.15
    total_amount = bill - dis
    print(f"Discount amount: {dis:.2f}")
    print(f"Total amount: {total_amount:.2f}")
except ValueError as e:
    print(f"Error: {e}")
except:
    print("An unexpected error occurred.")



