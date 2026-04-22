nums = [4, 15, 88, 59, 100]

largest = nums[0]
for n in nums:
    if n > largest:
        largest = n

print("Largest:", largest)