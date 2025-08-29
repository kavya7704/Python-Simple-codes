def maximumANDSum(nums, numSlots):
    n = len(nums)
    total_positions = numSlots * 2  # each slot can take 2 numbers
    dp = {}

    def solve(i, mask):
        if i == n:
            return 0
        if (i, mask) in dp:
            return dp[(i, mask)]

        best = 0
        for slot in range(1, numSlots+1):
            for pos in range(2):
                bit = (slot-1)*2 + pos
                if not (mask & (1 << bit)):  # if position free
                    new_mask = mask | (1 << bit)
                    best = max(best, (nums[i] & slot) + solve(i+1, new_mask))

        dp[(i, mask)] = best
        return best

    return solve(0, 0)

nums = [1, 2, 3, 4, 5, 6]
numSlots = 3
print(maximumANDSum(nums, numSlots))   
