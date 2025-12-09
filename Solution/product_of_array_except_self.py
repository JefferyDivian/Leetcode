def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leng = len(nums)
        pref_arr = [0]*leng
        suff_arr = [0]*leng

        prev_mul = 1
        for i in range(leng):
            prev_mul*=nums[i]
            pref_arr[i]=prev_mul
            
        suff_mul = 1
        for i in range(leng-1,0,-1):
            suff_mul*=nums[i]
            suff_arr[i]=suff_mul
            
        out = []
        for i in range(leng):
            left = pref_arr[i-1] if i>0 else 1
            right = suff_arr[i+1] if i<leng-1 else 1
            out.append(left * right)
        
        return out