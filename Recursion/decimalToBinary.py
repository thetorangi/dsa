def binary(n):
    if n == 0 :
        return n
    return  n%2 + binary(int(n/2))*10

print(binary(31))