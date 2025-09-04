# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

texts = ["apple orange apple", "banana apple orange", "banana grape"]

words = []
for sentence in texts:
    words.extend(sentence.split())

unique_words = set(words)

for word in unique_words:
    print(f"{word} -> {words.count(word)}")
