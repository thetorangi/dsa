def summ(n):
    if n <= 1:
        return n
    return (n%10) + summ(n//10)

print(summ(49527319465538237782))