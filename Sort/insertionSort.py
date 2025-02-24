def insSort(nums):
    
    for i in range(1,len(nums)):
        x=nums[i]
        j=i-1
        while j >= 0 and nums[j] > x :
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = x
         
print("Insertion Sort")

nums = [6,1,3,2,9,5,7]

insSort(nums)

print(nums)