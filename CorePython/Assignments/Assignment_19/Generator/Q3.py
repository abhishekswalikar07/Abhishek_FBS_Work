# Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

# def infinite_range():
#     n = 0
#     while True:
#         yield n
#         n += 1

# gen = infinite_range()
# for i in range(20):
#     print(next(gen), end=" ")


def my_range(start, stop, step):
    if step == 0:
        print("step argument must not be zero")
    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


for num in my_range(1, 10, 2):
    print(num, end=" ")

