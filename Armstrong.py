n = int(input())

def Armstrong(n):
    
    Sum = 0
    t = n
    while n > 0:
        Sum += ( n % 10) ** 3
        n //= 10
    
    return t == Sum
    
print(Armstrong(n))
