# Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

str1=input("Enter string:")
dict1={word:len(word) for word in str1.split()   }
print(dict1)