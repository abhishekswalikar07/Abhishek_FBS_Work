# Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

def find_pairs(numbers, target):
    pairs = []
    seen = set() 

    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs

numbers = [2, 4, 3, 5, 7, 8, 9]
target = 10

result = find_pairs(numbers, target)
print("Pairs with sum", target, ":", result)
