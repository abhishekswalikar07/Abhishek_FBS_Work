# Find all of the words in a string that are less than 5 letters (take input from user)

str1 = input("Enter string: ")
li = [word for word in str1.split() if len(word) < 5]
print("Words with less than 5 letters:", li)
