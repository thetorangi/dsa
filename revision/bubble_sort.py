print("---Bubble Sort---")


def bubbleSort(nums):
    for i in range(len(nums)-1):
        swapped = False
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1] , nums[j]
                swapped = True
        if not swapped :
            break
    return nums
    
    
nums = [5,3,2,17,3,55,34,21]

print(nums)

print(bubbleSort(nums))
