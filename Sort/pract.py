def insertionSort(nums):
    for i in range(1,len(nums)):
        x = nums[i]
        j=i-1
        while j>=0 and nums[j]>x:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=x

    return nums

def selectionSort(nums):
    for i in range(len(nums)):
        x=i
        for j in range(i+1,len(nums)):
            if nums[j] < nums [x]:
                x=j
        nums[x],nums[i]=nums[i],nums[x]

    return nums

def pivot(nums,piv_idx,end):
    swap=piv_idx
    for i in range(piv_idx+1,end+1):
        if nums[i] < nums[piv_idx]:
            swap+=1
            nums[swap],nums[i]=nums[i],nums[swap]
    nums[swap],nums[piv_idx]=nums[piv_idx],nums[swap]
    return swap

def quickSort(nums,left,right):
    if left < right:
        piv = pivot(nums,left,right)
        quickSort(nums,left,piv-1)
        quickSort(nums,piv+1,right)
    return nums

def merge(left,right):
    i=j=0
    comb=[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            comb.append(left[i])
            i+=1
        else:
            comb.append(right[j])
            j+=1
    
    while i < len(left):
        comb.append(left[i])
        i+=1
    
    while j < len(right):
        comb.append(right[j])
        j+=1

    return comb
    

def mergeSort(nums):
    if len(nums) == 1:
        return nums
    mid = int (len(nums)/2)
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left,right)

nums = [65,33,21,87,34,89,55]

# print(insertionSort(nums))

# print(selectionSort(nums))

# print(quickSort(nums,0,len(nums)-1))

print(mergeSort(nums))