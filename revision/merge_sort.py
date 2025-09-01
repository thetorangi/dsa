print("--- Merge Sort ---\n")

def helper(left,right):
    l=r=0
    res=[]
    while l < len(left) and r < len(right):
        if left[l]<right[r]:
            res.append(left[l])
            l+=1
        else:
            res.append(right[r])
            r+=1
    
    while l < len(left):
        res.append(left[l])
        l+=1
    
    while r < len(right):
        res.append(right[r])
        r+=1
    
    return res

def merge_sort(nums):
    if len(nums)==1:
        return nums
        
    mid = (len(nums)//2)
    
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    
    return helper(left,right)


nums = [9,8,7,6,5,4,3,2,1,2,3,4,5]

print(f"Before Sorting \n{nums}\n")


print(f"After Sorting \n{merge_sort(nums)}")
