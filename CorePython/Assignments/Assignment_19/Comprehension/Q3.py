# Count the number of spaces in a string (take input from user)


str1 = input("Enter String: ")
print("Number of spaces:", len([ch for ch in str1 if ch == " "]))
