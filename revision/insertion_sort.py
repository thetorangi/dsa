print("---Insertion Sort----")

def insertion_sort(nums):
    for i in range(1,len(nums)):
        x = nums[i]
        j=i-1
        while j>=0 and nums[j]>x:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=x
    return nums
            

nums = [2,8,5,1,4,9,3]

print("-Before Sorting-")
print(nums)

print("-After Sorting-")
insertion_sort(nums)

print(nums)
