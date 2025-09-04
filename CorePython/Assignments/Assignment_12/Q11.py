#  Python Program to replace every blank space with hyphen in a string.

def strReplace(str):
    result="" 
    is_space=False
    for ch in str:
        if ch==" ":
            result+="-"
            is_space=True
        else:
            result+=ch
    if not is_space:
        print(f'{str} has no space.')
    return result
str=input("Enter a string:")
print(f'{str} after replacing space by - is : {strReplace(str)}')