def twoSumII(numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        loc = {}
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t not in loc:
                loc[numbers[i]] = i
            else:
                first = loc[t]
                second = i
                
        return [first+1,second+1]