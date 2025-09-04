# Python Program to Check if a Given Key Exists in a Dictionary or Not

d = {1: "apple", 2: "banana", 3: "cherry"}

key = int(input("Enter key to check: "))

if key in d:
    print(f"Key {key} exists in dictionary with value {d[key]}")
else:
    print(f"Key {key} does not exist in dictionary")
