def countSort(nums):
    
    maxx = max(nums)
    
    res = [0 for _ in range(maxx+1)]
    
    for num in nums:
        res[num]+=1
    
    op=[]
    for i in range(len(res)):
        if i:
            x = res[i]
            while x:
                op.append(i)
                x-=1
  
    return op
    
arr = [8,8,6,5,3,1,5,1,7]
ans = countSort(arr)

print(ans)
