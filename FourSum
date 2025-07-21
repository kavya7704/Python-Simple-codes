#four pointer for sorted array
def Sum4(nums,t):
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(0,n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                if s == t:
                    temp = [nums[i] , nums[j] , nums[k] , nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1
                elif s > t:
                    l -= 1
                else:
                    k += 1
    return ans 
print(Sum4([2,2,2,2],8))

#FourSum
def Four_Sum(nums,t):
    n = len(nums)
    quadruplets = set()

    for i in range(0,n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == t:
                        temp = [nums[i] , nums[j] , nums[k] , nums[l]]
                        temp.sort()
                        quadruplets.add(tuple(temp))
    res = []
    for t in quadruplets:
        res.append(list(t))
    return res
