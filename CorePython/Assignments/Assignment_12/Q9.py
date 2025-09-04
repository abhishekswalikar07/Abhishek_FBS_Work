# Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

def cal_words_char(str):
    word=0
    char=0
    
    for ch in str: 
        if ch!=" ":
            char+=1
        if ch==" ":
            word+=1
            
    if char > 0:
        word += 1
    if word==0 and char==0:
        print(f'{str} has no words and characters')
    return word, char
str=input("Enter string:")
print(f'Total number of words and characters in {str} is {cal_words_char(str)}')   