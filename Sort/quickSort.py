def pivot(nums,pivot_idx,end):
    swap = pivot_idx
    for i in range(pivot_idx+1,end+1):
        if  nums[i] < nums[pivot_idx] :
            swap+=1
            nums[swap],nums[i] = nums[i] , nums[swap]
    nums[swap],nums[pivot_idx] = nums[pivot_idx] , nums[swap]
    return swap

def quickSort(nums,left,right):
    if left < right:
        piv_idx = pivot(nums,left,right)
        quickSort(nums,left,piv_idx-1)
        quickSort(nums,piv_idx+1,right)
    return nums

nums = [8,2,6,1,5,3,9,4]

print(quickSort(nums,0,len(nums)-1))