def moveZeroes(nums):

    n = len(nums)
    left = 0

    
    for i in range(n):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1
    for i in range(left, n):
        nums[i] = 0

    return nums

##Example 1:
nums = [0, 1, 0, 3, 12]
result = moveZeroes(nums)
print(result)

##Example 2:
##nums = [0]
##result = moveZeroes(nums)
##print(result)

  
