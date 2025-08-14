# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)


import random

id=1
pwd=12345

userid=int(input("Enter userid:"))
password=int(input("Enter password:"))

captcha =random.randint(1111,9999)

print(captcha)

captcha_enter=int(input("Enter given captcha:"))


if id==userid and pwd==password:
    if captcha_enter==captcha:
        print("Valid userid and password")
    else:
        print("Invalid captcha")
else:
    print("InValid userid and password")