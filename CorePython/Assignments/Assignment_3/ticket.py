#Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

age1=int(input("Enter first person age:"))
age2=int(input("Enter second person age:"))
age3=int(input("Enter third person age:"))
age4=int(input("Enter fourth person age:"))
age5=int(input("Enter fifth person age:"))

tkt_amt=int(input("Enter ticket amount:"))

if age1<12:
    dis_amt=tkt_amt*0.3
    amt1=tkt_amt-dis_amt
elif age1>59:
    dis_amt=tkt_amt*0.5
    amt1=tkt_amt-dis_amt
else:
    amt1=tkt_amt
    
    
    
if age2<12:
    dis_amt=tkt_amt*0.3
    amt2=tkt_amt-dis_amt
elif age2>59:
    dis_amt=tkt_amt*0.5
    amt2=tkt_amt-dis_amt
else:
    amt2=tkt_amt
    
    

if age3<12:
    dis_amt=tkt_amt*0.3
    amt3=tkt_amt-dis_amt
elif age3>59:
    dis_amt=tkt_amt*0.5
    amt3=tkt_amt-dis_amt
else:
    amt3=tkt_amt
    
    

if age4<12:
    dis_amt=tkt_amt*0.3
    amt4=tkt_amt-dis_amt
elif age4>59:
    dis_amt=tkt_amt*0.5
    amt4=tkt_amt-dis_amt
else:
    amt4=tkt_amt
    
    

if age5<12:
    dis_amt=tkt_amt*0.3
    amt5=tkt_amt-dis_amt
elif age5>59:
    dis_amt=tkt_amt*0.5
    amt5=tkt_amt-dis_amt
else:
    amt5=tkt_amt
    
    
Total_amt=amt1+amt2+amt3+amt4+amt5

print(f'Total amount of ticket for five people is {Total_amt} ')
