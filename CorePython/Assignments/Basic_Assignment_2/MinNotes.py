#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.


amt=int(input("Enter amount:"))

Two_Thousnd=amt//2000  #2885//2000=1
Rem_amt=amt%2000        # 2885%2000=885

Five_Hundred=Rem_amt//500  #885//500=1

Rem_amt=Rem_amt%500  #885%500=385

Two_Hundred=Rem_amt//200   #385//200=1
Rem_amt=Rem_amt%200        #385%200=185

Hundred=Rem_amt//100     #185//100=1
Rem_amt=Rem_amt%100     #185%100=85

Fifty=Rem_amt//50       # 85//50=1
Rem_amt=Rem_amt%50      #85 %50=35

Twenty=Rem_amt//20      #35 //20=1
Rem_amt=Rem_amt%20      #35%20=15

Ten=Rem_amt//10         #15//10=1
Rem_amt=Rem_amt%10      #15%10=5

Five=Rem_amt//5         #5//5=1
Rem_amt=Rem_amt%5       #5%5=0

print(f'Notes of Two_Thousand:{Two_Thousnd}, Five_Hundred:{Five_Hundred}, Two_Hundred:{Two_Hundred}, Hundred:{Hundred}, Fifty:{Fifty}, Twenty:{Twenty}, Ten:{Ten}, Five:{Five}.')