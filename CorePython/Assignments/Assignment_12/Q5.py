# Python Program to Count the Number of Vowels in a String


def vowelCount(str):
    count=0

    for ch in str.lower():
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            count+=1
    if count==0:
        print(f'{str} does not have vowels')
    return count   
str=input("Enter a string:")
print(f'Total number of vowels in {str} : {vowelCount(str)}')