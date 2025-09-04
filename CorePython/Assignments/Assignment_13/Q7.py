# Python Program to Remove the Given Key from a Dictionary

d = {1: "apple", 2: "banana", 3: "cherry"}

key = int(input("Enter the key to remove: "))

if key in d:
    d.pop(key)   
    print("Updated Dictionary:", d)
else:
    print(f"Key {key} not found in dictionary")
