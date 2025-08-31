print("---Selection Sort---")


def selection_sort(nums):
    for i in range(len(nums)):
        minn = i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minn]:
                minn = j
        nums[minn],nums[i] = nums[i],nums[minn]
    return nums
    
print("--Before Sorting--")
nums = [5,3,2,17,3,55,34,21]
print(nums)
print("--After Sorting--")
print(selection_sort(nums))
