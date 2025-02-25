print("Merge Sort")

def merge(list1,list2):
    i=j=0
    combined = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    
    while i < len(list1):
        combined.append(list1[i])
        i+=1

    while j < len(list2):
        combined.append(list2[j])
        j+=1

    return combined

def mergeSort(nums):
    if len(nums) == 1:
        return nums
    mid = int(len(nums)/2)
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left,right)



nums = [5,2,7,1,3,9,4]

print(mergeSort(nums))