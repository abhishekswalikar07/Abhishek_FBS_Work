import re
str=r'''Firstbit solution is an educational & placement institute.
Firstbit is located in pune'''
pattern=re.compile(r'Firstbit')
result=re.findall(pattern,str)
print(result)