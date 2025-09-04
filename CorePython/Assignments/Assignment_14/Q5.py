# Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

def longest_common_prefix(words):
    prefix = ""
    if not words:
        return prefix

    for i in range(len(min(words, key=len))):  
        chars = {word[i] for word in words}  
        if len(chars) == 1:                  
            prefix += chars.pop()
        else:
            break
    return prefix

words = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(words))
