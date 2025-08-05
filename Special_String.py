A = input()
S = input()

def ASCII(A,S):
    c1 = 0 
    for i in A:
        if i in S:
            c1 += 1
    if c1 == len(A):
        return 0 
    else:
        count = 0
        for i in range(len(A)):
            min_distance = float('inf')
            for j in range(0,len(S)):
                min_distance = min(min_distance ,abs(ord(A[i]) - ord(S[j])))
            count += min_distance
        return count 
    
print(ASCII(A,S))
