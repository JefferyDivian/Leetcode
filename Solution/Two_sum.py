def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    vals = {}
    for i in range(len(nums)):
        remaining = target - nums[i]
        if remaining not in vals:
            vals[nums[i]] = i
        elif remaining in vals:
            first = vals[remaining]
            second = i

    return(first,second) 