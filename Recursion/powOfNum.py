def power(num,poww):
    assert poww >= 0 and int(poww) == poww , "Enter a positive integer number"
    if num <=1 or poww <=0:
        return 1
    return num * power(num,poww-1)
print(power(8,1))
    