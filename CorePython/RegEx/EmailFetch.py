
import re

data="""101 Adinath 25 adinat@gmail.com
102 Onkar 27 onkar@gmail.co.in
103 Mayur 35 mayur@yahoo.com
104 Abhishek 23 walikarabhishek85@gmail.com"""

# result=re.findall(r'\w+\.?\w*@\w+\.\w+\.?\w+',data)
# result=re.findall(r'[\w.]+@[\w.]+\w+',data)
result=re.findall(r'[\w.]+@[\w.]+',data)

print(result)