# Python program to replace all occurrences of 'a' with '$' in a string

text = input("Enter a string: ")

result = ""

for ch in text.lower():
    if ch == 'a':   
        result += '$'
    else:
        result += ch

print("Modified string:", result)
