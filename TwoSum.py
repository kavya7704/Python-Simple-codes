#using dict
def two(nums,t):
        d = {}# SC - O(N)
        n = len(nums)
        for a in range(0,n):#TC - O(N)
            b = t - nums[a]
            if b in d:
                return [a,d[b]]
            else:
                d[nums[a]] = a
print(two([1,2,3,1,4],7))

#using sorted array and two pointer
def twoSum(nums,t):
    n = len(nums)
    low = 0
    high = n - 1
    while low < high:#TC - O(logN)
        s = nums[low] + nums[high]
        if s == t:
            return True
        elif s > t:
            high -= 1
        else:
            low += 1
    return False
print(twoSum([1,2,3,1,4],7))
