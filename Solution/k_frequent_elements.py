def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    counts = {}
    for i in nums:
        if i in counts:
            counts[i]+=1
        else:
            counts[i]=1

    return list(dict(sorted(counts.items(),key = lambda x:x[1],reverse=True)[:k]).keys())