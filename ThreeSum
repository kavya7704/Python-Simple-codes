#optimal
def three_Sum(nums):
    n = len(nums)
    triplet_Sum = set()
    for i in range(0,n-1):# TC : O(N^2)
        hashmap = [] #SC : O(N)
        for j in range(i+1,n):
            k = -(nums[i]+nums[j])
            if k in hashmap:     
                temp = [nums[i],nums[j],k]
                temp.sort()
                triplet_Sum.add(tuple(temp))
            hashmap.append(nums[j])
    ans = []
    for t in triplet_Sum:
        ans.append(list(t))
    return ans
print(three_Sum([3,2,0,1,-1]))

#three pointer only when the array is sorted
def three_Sum(nums):
    n = len(nums)
    ans = []
    for i in range(0,n):#TC : O(logN)
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            Sum = nums[i] + nums[j] + nums[k]
            if Sum == 0:
                temp = [nums[i] , nums[j] , nums[k]]
                ans.append(temp)
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif Sum < 0:
                j += 1
            else:
                k -= 1
    return ans
print(three_Sum([3,2,0,1,-1]))'''
