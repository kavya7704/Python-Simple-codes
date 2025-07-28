def subset(nums):
    ans = []
    curr = []
    i = 0
    
    def gen(i,curr,ans,nums):
        if i == len(nums):
            ans.append(curr[:]) #can use curr.copy()
            return
        curr.append(nums[i])
        gen(i+1,curr,ans,nums) #left
        curr.pop()
        gen(i+1,curr,ans,nums) # right
    gen(i,curr,ans,nums)

    return ans

subset([1,2,3])
