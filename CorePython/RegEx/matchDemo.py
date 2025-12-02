import re

data="""101 Adinath 25 adinat@gmail.com
102 Onkar 27 onkar@gmail.co.in
103 Mayur 35 mayur@yahoo.com """

result=re.match(r'\d{2}',data)#Match at starting of string or data
print(result)