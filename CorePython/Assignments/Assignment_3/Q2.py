# Write a program to input any alphabet and check whether it is vowel or consonant.

alp=input("Enter alphabet character:")

if alp in 'aeiouAEIOU':
    print(f'{alp} is a vowel ')
else:
    print(f'{alp} is consonent.')
    