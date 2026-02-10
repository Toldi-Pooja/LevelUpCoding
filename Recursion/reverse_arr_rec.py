def reverse_arr(arr,left,right):
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    reverse_arr(arr,left+1,right-1)
def func(nums,l,r):
    reverse_arr(nums,l,r)
    return nums
nums = list(map(int,input().split()))
print(func(nums,0,len(nums)-1))