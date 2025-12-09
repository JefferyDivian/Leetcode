def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    sort_strs = [''.join(sorted(i)) for i in strs]
    hashs = {}
    for i,j in zip(strs,sort_strs):
        if j not in hashs:
            hashs[j] = [i] 
        else:
            hashs[j].append(i)
        
    return(list(hashs.values()))