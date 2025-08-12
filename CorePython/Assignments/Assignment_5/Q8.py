# Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a*2 / 2 + a*3 / 3 + ...... + a*10 / 10 
# e. x - x*2/3 + x*3/5 - x*4/7 + .... to n terms


# a: 1! + 2! + 3! + 4! + .....n!

n = int(input("Enter n: "))

sum_fact = 0
fact = 1

for i in range(1, n + 1):
    fact *= i          
    sum_fact += fact

print("Sum of factorial series =", sum_fact)


# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

N = int(input("Enter N: "))

sum_exp = 0
for i in range(1, N + 1):
    sum_exp += N ** i

print("Sum of exponent series =", sum_exp)


# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter number of terms: "))

sum_geo = 0
term = 1
for i in range(n):
    sum_geo += term
    term *= 2

print("Sum of geometric series =", sum_geo)



# d. S = a + a*2 / 2 + a*3 / 3 + ...... + a*10 / 10 

a = float(input("Enter value of a: "))

sum_series = 0
for i in range(1, 11):
    sum_series += (a * i) / i   # simplifies to 'a', but keeping formula

print("Sum of series =", sum_series)


# e. x - x*2/3 + x*3/5 - x*4/7 + .... to n terms

x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum_series = 0
sign = 1
denominator = 1

for i in range(1, n + 1):
    sum_series += sign * (x * i / denominator)
    sign *= -1         # alternate + and -
    denominator += 2   # odd denominators: 1, 3, 5, ...

print("Sum of alternating series =", sum_series)






