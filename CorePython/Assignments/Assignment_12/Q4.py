# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

def exchange_first_last(s):
    if len(s) <= 1:   
        return s

    result = ""
    
    result += s[len(s) - 1]
  
    for i in range(1, len(s) - 1):
        result += s[i]

    result += s[0]

    return result
string = input("Enter string:").lower()
print("Original String:", string)
print("Modified String:", exchange_first_last(string))
