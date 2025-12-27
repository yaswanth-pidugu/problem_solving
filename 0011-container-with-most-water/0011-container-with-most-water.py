class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        L = 0 
        R = len(height)-1
        while L < R:
            w = R - L
            h = min(height[L], height[R])
            area = w*h
            max_area = max(area, max_area)
            if height[L] < height[R]:
                L+=1
            else:
                R-=1
        return max_area