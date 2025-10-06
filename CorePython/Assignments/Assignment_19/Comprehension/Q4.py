# Remove all of the vowels in a string (take input from user)

str1 = input("Enter String: ")
li =([ch for ch in str1 if ch.lower() not in 'aeiou'])
print("String after removing vowels:",''.join(li))
