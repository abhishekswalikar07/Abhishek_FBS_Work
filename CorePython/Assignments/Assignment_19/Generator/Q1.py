# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.


def fibonacci():
    a, b = 0, 1
    while True:      
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for i in range(10):
    print(next(fib_gen), end=" ")




