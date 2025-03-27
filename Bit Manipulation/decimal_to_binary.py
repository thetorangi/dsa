n = 31

res =""

while n :
    res+='1' if n%2==1 else '0'
    n=n>>1

res = res[::-1]
print(res)