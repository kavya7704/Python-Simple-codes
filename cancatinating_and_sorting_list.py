def Sort(nums1,nums2):
    i , j = 0 , 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1

    while i < len(nums1):
        res.append(nums1[i])
        i += 1

    while j < len(nums2):
        res.append(nums2[j])
        j += 1

    return res
print(Sort([1,1,2,2,3,4,6,7],[1,3,6,8,9]))
