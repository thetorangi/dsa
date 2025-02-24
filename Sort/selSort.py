def selSort(nums):
    for i in range(len(nums)):
        x=i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[x]:
                x = j
        if x != i:
            nums[x],nums[i]=nums[i],nums[x]


print("Selection Sort")

nums = [6,4,3,1,9,5,7]

selSort(nums)

print(nums)