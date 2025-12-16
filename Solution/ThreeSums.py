def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        answer = []

        for i,a in enumerate(nums):
            l = i+1
            r = len(nums)-1
            while l<r:
                sums = a + nums[l] + nums[r]
                if sums < 0:
                    l+=1
                elif sums > 0:
                    r-=1
                else:
                    if [a,nums[l],nums[r]] not in answer:
                        answer.append([a,nums[l],nums[r]])
                    l+=1

        return (answer)

