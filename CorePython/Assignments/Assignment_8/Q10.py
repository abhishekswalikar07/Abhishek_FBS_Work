#  Write a program to check if entered year is a leap year or not.


def isLeapYear(year):
    if (year % 400 == 0  and year % 100 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")

year = int(input("Enter a year: "))
isLeapYear(year)
