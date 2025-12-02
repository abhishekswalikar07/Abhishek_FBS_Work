import re

str=r"""Firstbit solutions is an educational institute.
400+ companies in campus..."""

#\w-aplhanumeric and underscore(_)
result=re.findall(r'\w',str)

result=re.findall(r'\W',str)

result=re.findall(r'\d',str)

result=re.findall(r'\D',str)

result=re.findall(r'\s',str)

result=re.findall(r'\S',str)

result=re.findall(r'\w{3}',str)

result=re.findall(r'\w+',str)

result=re.findall(r'\w*',str)

result=re.findall(r'\w?',str)

result=re.findall(r'[abc]',str)

result=re.findall(r'a|b',str)

result=re.findall(r'^\w',str)

result=re.findall(r'\W$',str)

result=re.findall(r'^\w',str,re.M)

result=re.findall(r'firstbit',str, re.I)
result=re.findall(r'\W',str,re.M|re.I)
print(result)