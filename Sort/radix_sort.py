def counting_sort(nums,exp):
    n = len(nums)
    
    op = [0] * n 

    cnt = [0] * (10)
    
    for i in range(0,n):
        idx = nums[i] // exp
        cnt[idx%10] += 1
    # print(cnt)
        
    for i in range(1,10):
        cnt[i] += cnt[i-1]
        
    i = n - 1
    while i >= 0 :
       idx = nums[i] // exp
       op[cnt[idx%10]-1] = nums[i]
       cnt[idx%10]-=1
       i-=1
       
        
    i=0
    for i in range(len(nums)):
        nums[i]=op[i]
    
    
def radix_sort(nums):
    maxx = max(nums)
    exp=1
    while maxx/exp >=1 :
        counting_sort(nums,exp)
        exp *= 10


nums = [654,234,78,90,7,32,567,21,87]

print(f"Before sorting {nums}")

radix_sort(nums)


print(f"After sorting {nums}")
