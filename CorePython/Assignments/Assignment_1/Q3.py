#Program to find quotient and remainder of two numbers.

dividend=int(input("Enter value for dividend: "))
divisor=int(input("Enter value for divisor: "))

quotient=dividend // divisor
remainder=dividend % divisor

print(f'Quotient and remainder for dividend{dividend} and divisor{divisor} is {quotient}, {remainder}')


