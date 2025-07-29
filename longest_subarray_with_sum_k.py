def longestSubarray(arr,k):
    n = len(arr)
    d = {}
    #temp = []
    Sum,maxLen = 0,0
    for i in range(0,n):
        Sum += arr[i]
        if Sum == k:
            maxLen = i + 1
            #temp = arr[0:i + 1]
        rem = Sum - k
        if rem in d and maxLen < i-d[rem]:
            maxLen = i-d[rem]
            #temp = arr[d[rem]:i + 1]
        if Sum not in d:
            d[Sum] = i
    return maxLen
print(longestSubarray([2,0,0,3], k = 2))
