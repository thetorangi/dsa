print("3 Stack in 1 List")

nums = [1,2]

leng = len(nums)

s1=[]
s2=[]
s3=[]
s2=[]
s3=[]

for i in range(leng):
    if i < leng/3:
        s1.append(nums[i])
    elif i < 2*( leng/3 ):
        s2.append(nums[i])
    else :
        s3.append(nums[i])

print(s1)
print(s2)
print(s3)


