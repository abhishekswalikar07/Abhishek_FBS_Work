# Python Program to count the occurrences of ach word in a string.

#1.
def count_ach(s):
    words = s.split()  
    count = 0
    for word in words:
        if word.lower() == "ach":  
            count += 1
    return count


s = input("Enter a string: ")
print(f"Occurrences of 'ach' in '{s}' : {count_ach(s)}")

#2. 


def word_count(s):
    counts = {}
    word = ""
    for ch in s + " ":   
        if ch != " ":
            word += ch
        else:
            if word:   
                word_lower = word.lower()
                counts[word_lower] = counts.get(word_lower, 0) + 1
                word = ""
    return counts

s = input("Enter a string: ")
counts = word_count(s)

print("Word occurrences:")
for word, count in counts.items():
    print(f"{word}: {count}")




    