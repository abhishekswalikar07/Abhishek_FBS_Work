#  Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

def word_frequency(s):
    freq = {}
    words = s.split()  
    
    for word in words:
        word = word.lower()   
        freq[word] = freq.get(word, 0) + 1
    
    return freq

s = input("Enter a string: ")
result = word_frequency(s)

print("Word Frequency:")
for word, count in result.items():
    print(f"{word}: {count}")
