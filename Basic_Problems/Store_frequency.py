def Store_frequency(nums):
    di = { }
    n = len(nums)
    for i in range(0,n):
        if nums[i] in di :
            di[nums[i]]+=1
        else:
            di[nums[i]]=1
    return di
nums = list(map(int,input().split()))
print(Store_frequency(nums))