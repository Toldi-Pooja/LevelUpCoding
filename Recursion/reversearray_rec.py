def palindrome(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    palindrome(nums, left+1, right-1)

nums = [5,1,2,6,7,3,4,8]
left = 0
right = len(nums)-1
palindrome(nums, left, right)
print(nums)
