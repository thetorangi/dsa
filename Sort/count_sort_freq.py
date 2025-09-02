def countSort(nums):
    
    maxx = max(nums)
    res=[]
    freq = {}
    
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    # print(freq)
    
    for i in range(maxx+1):
        if i in freq.keys():
            x = freq[i]
            while x:
                res.append(i)
                x-=1
    return res
        
        
    
arr = [8,8,6,5,3,1,5,1,7]
print(arr)
ans = countSort(arr)
print(ans)
