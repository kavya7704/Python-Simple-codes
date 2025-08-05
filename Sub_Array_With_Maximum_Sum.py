n = int(input())
nums = list(map(int,input().split()))

def Maximum_sum(n,nums):
    max_score = nums[0]
    current_score = nums[0]
    for i in range(1,n):
        current_score = max(nums[i],current_score + nums[i])
        max_score = max(max_score,current_score)
        
    return max_score
    
print(Maximum_sum(n,nums))
