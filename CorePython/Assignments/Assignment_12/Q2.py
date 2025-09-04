# Python Program to Remove the nth Index Character from a Non-Empty String


def remove_char(s, n):
    if n < 0 or n >= len(s):
        return "Index out of range"

    result = ""
    for i in range(len(s)):
        if i != n:   
            result += s[i]
    return result


string = input("Enter a string:")
n = int(input("Enter index number of character to remove from string:")) 

print("Original String:", string)
print("After Removal :", remove_char(string, n))
