# Python Program to Detect if Two Strings are Anagrams

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
 
    count = {}
    for ch in str1:
        count[ch] = count.get(ch, 0) + 1 # Checks whether ch is present in dict then returns its value else bydefault it gives default_value

    for ch in str2:
        if ch not in count:
            return False
        count[ch] -= 1

    for value in count.values():
        if value != 0:
            return False
    return True

s1 = "triangle".lower()
s2 = "integral".lower()

if are_anagrams(s1, s2):
    print(f"Yes, {s1} and {s2} are anagrams")
else:
    print("No, {s1} and {s2} are not anagrams")
