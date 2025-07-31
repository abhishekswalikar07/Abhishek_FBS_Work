amt=int(input("Enter amount:"))
Two_Thousnd=amt//2000

Rem_amt=amt%2000

Five_Hundred=Rem_amt//500

Rem_amt=Rem_amt%500

Two_Hundred=Rem_amt//200
Rem_amt=Rem_amt%200

Hundred=Rem_amt//100
Rem_amt=Rem_amt%100

Fifty=Rem_amt//50
Rem_amt=Rem_amt%50

Twenty=Rem_amt//20
Rem_amt=Rem_amt%20

Ten=Rem_amt//10
Rem_amt=Rem_amt%10

Five=Rem_amt//5
Rem_amt=Rem_amt%5

print(f'Notes of Two_Thousand:{Two_Thousnd}, Five_Hundred:{Five_Hundred}, Two_Hundred:{Two_Hundred}, Hundred:{Hundred}, Fifty:{Fifty}, Twenty:{Twenty}, Ten:{Ten}, Five:{Five}.')