# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def three_sum(nums, target):
    result = set()  
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)  
    return list(result)

numbers = [1, 2, -1, 0, -2, 1]
target = 0
print("Unique triplets:", three_sum(numbers, target))
