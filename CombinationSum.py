def combinationSum(candidates,target):
    curr = []
    ans = []
    
    def gen(ind, curr, ans, candidates, target):
        if target == 0:
            ans.append(curr.copy())
            return
        if target < 0:
            return 
        if ind == len(candidates):
            return
    
        curr.append(candidates[ind])
        gen(ind, curr, ans, candidates, target - candidates[ind])

        curr.pop()
        gen(ind + 1, curr, ans, candidates, target)
    gen(0,curr, ans, candidates, target)
    return ans

print(combinationSum([2,3,6,7],5))
