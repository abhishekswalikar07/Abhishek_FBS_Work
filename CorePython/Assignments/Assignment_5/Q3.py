# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n=int(input("Enter total number of passengers:"))
tkt_cost=int(input("Enter per ticket cost:"))

total_amt=0

for i in range(1, n+1):
    age=int(input(f"Enter age of passenger {i}: "))
    tkt_amt=0
    amount=0
    if age<=12:
        tkt_amt=tkt_cost*0.7
    elif age>59:
        tkt_amt=tkt_cost*0.5
    else:
        tkt_amt=tkt_cost
    
    amount+=tkt_amt

    total_amt+=amount

print(f'Total amount for {n} passengers is {total_amt} Rs')