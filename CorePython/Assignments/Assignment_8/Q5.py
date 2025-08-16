# Sum of all prime numbers between 1 to n
            
def primeSum(n):
    sum = 0
    num = 2
    while num <= n:   # loop until n
        for i in range(2, (num // 2) + 1):  # check if num is prime
            if num % i == 0:
                break
        else:
            sum += num   # add the prime number
        num += 1        # move to next number
    print(f'Sum of all prime numbers from 1 to {n} is {sum}')

a = int(input("Enter last limit of numbers: "))
primeSum(a)

        