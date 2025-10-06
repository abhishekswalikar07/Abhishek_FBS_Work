# Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.


def palindrome_generator():
    n = 10
    while True:
        if str(n) == str(n)[::-1]:  
            yield n
        n += 1

# Example usage: print first 20 palindrome numbers
gen = palindrome_generator()
for _ in range(20):
    print(next(gen), end=" ")
