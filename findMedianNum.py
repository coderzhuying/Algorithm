def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    l = len(nums)
    if l % 2 == 1:
        median_num = nums[int(l/2)]
    else:
        median_num = (nums[int(l/2) - 1] + nums[int(l/2)]) / 2
    return median_num


print(findMedianSortedArrays([1, 2], [3, 4]))