def sum_list(nums):
    total = 0 
    for n in nums:
        total += n
    return total
numbers = [1, 2, 3, 4, 5]
print("sum:", sum_list(numbers))