'''Arnab has given me a challenge. I have to calculate the number of numbers which are less than a certain value n, and 
have exactly k set bits in its binary form. As you are a Prepster like me, help me write a code that will take input for n and k 
and give the expected output.'''

n, k = map(int, input().split())
def set_bit(n,k):
    count = 0
    num = 1
    while num < n:
        if bin(num).count("1") == k:
            count += 1
        num += 1
    return count
    
print(set_bit(n,k))
