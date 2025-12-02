import re

data="""101 Adinath 25 adinat@gmail.com
102 Onkar 27 onkar@gmail.co.in
103 Mayur 35 mayur@yahoo.com """

result=re.finditer(r' \d{2} ',data)
for f in result:
    # print(f)
    # print(f.span())
    print(f.group())