# Python Program to find larger string without using built-in functions.

def large_string(str1, str2):
    count1=0
    count2=0
    
    for ch in str1:
        if ch !=" ":
         count1+=1
        
    for ch in str2:
        if ch !=" ":
            count2+=1
    
    if count1==count2:
        print(f'{str1} and {str2} have same length of string')
    elif count1>count2:
        print(f'{str1} is larger string')
    else:
        print(f'{str2} is larger string')
        
str1=input("Enter first string:")
str2=input("Enter second string:")

large_string(str1, str2)