#  Python Program to count number of lowercase characters in a string.

def count_lowercase(s):
    count = 0
    for ch in s:
        if ch.islower():  
            count += 1
    return count

s = input("Enter a string: ")
print(f"Total number of lowercase characters in '{s}' is: {count_lowercase(s)}")
