# Python Program to Calculate the Length of a String Without Using a
# Library Function

def string_length(str):
    count = 0
    for ch in str:
        count += 1
    return count

str=input("Enter string:")
print(f'The length of {str} is {string_length(str)}')    