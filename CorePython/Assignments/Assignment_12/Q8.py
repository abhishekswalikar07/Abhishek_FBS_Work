# Python Program to Remove the Characters of Odd Index Values in a String



def remove_odd_index_chars(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:   
            result += s[i]
    return result

s = input("Enter a string: ")
print(f"Original String: {s}")
print(f"After Removing Odd Index Characters: {remove_odd_index_chars(s)}")
