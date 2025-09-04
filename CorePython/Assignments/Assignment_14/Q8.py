# Write a Python program to find all the anagrams and group them
# together from a given list of strings.

def group_anagrams(words):
    groups = {}  
    
    for word in words:
        key = ''.join(sorted(word))  
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Grouped Anagrams:", group_anagrams(words))
