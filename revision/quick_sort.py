print("--- Quick Sort ---")

def helper(nums,start,end):
    l = start
    for i in range(start+1,end+1):
        if nums[start] > nums[i]:
            l+=1
            nums[l],nums[i] = nums[i],nums[l]
    nums[start],nums[l]=nums[l],nums[start]
    return l

def quick_sort(nums,start,end):
    if start < end :
        piv = helper(nums,start,end)
        quick_sort(nums,start,piv-1)
        quick_sort(nums,piv+1,end)
    return nums

nums = [2, 8, 5, 1, 4, 9, 3]

quick_sort(nums,0,len(nums)-1)

print(nums)
