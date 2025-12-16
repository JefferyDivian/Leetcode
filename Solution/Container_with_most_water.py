
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    capacity = 0
    left = 0 
    right = len(height)-1  

    while left < right:
        cap = min(height[left],height[right]) 
        gap = abs(right - left) 
        cur_capacity = cap * gap 

        if cur_capacity > capacity :
            capacity = cur_capacity
            if height[right]>height[left]:
                left+=1
            else:
                right-=1

        else:
            if height[right]>height[left]:
                left+=1
            else:
                right-=1

    return capacity

    