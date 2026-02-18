def find_max(nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
        return max
numbers = [3, 5, 2, 8, 1]
print("max:", find_max(numbers))