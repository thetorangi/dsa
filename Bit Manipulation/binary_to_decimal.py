num = '11111'

n = 0 
p = 1

for i in range(len(num)-1,-1,-1):
    if num[i] == '1' :
        n += p
    p=p*2

print(n)
    