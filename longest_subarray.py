def longest_subarray_sum_k(arr, k):
    prefix_sum = 0
    hashmap = {}
    max_len = 0

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum == k:
            max_len = max(max_len, i + 1)
        
        if (prefix_sum - k) in hashmap:
            max_len = max(max_len, i - hashmap[prefix_sum - k])

        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i

    return max_len

print(longest_subarray_sum_k([10, 5, 2, 7, 1, 9], 15)) 
