Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

***********************************************

 def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        a = 0
        b = 0
        count = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= a:
                    a = height[l]
                else:
                    count += a - height[l]
                l +=1
            else:
                if height[r] >= b:
                    b = height[r]
                else:
                    count += b- height[r]
                r -=1
        return count
                 
                    
