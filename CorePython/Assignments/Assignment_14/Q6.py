# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.


def max_product_pair(nums):
    nums = list(set(nums))  
    
    nums.sort()
  
    prod1 = nums[-1] * nums[-2]
    prod2 = nums[0] * nums[1]

    if prod1 > prod2:
        return (nums[-2], nums[-1]), prod1
    else:
        return (nums[0], nums[1]), prod2


# Example usage
numbers = [1, 20, -5, 4, -6, 30]
pair, product = max_product_pair(numbers)
print("Pair with maximum product:", pair)
print("Maximum product:", product)

