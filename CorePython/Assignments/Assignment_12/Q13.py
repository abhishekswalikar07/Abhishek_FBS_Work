# Python Program to count number of digits and letters in a string.

def count_digits_letters(s):
    digits = 0
    letters = 0

    for ch in s:
        if ch.isdigit():
            digits += 1
        elif ch.isalpha():
            letters += 1
    return digits, letters

s = input("Enter a string: ")
d, l = count_digits_letters(s)
print(f"Total letters: {l}")
print(f"Total digits: {d}")
