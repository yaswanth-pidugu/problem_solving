class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        res = [0]*n
        for i in range(n-1,-1,-1):
            ls = nums[l]**2
            rs = nums[r]**2
            if ls > rs:
                res[i] = ls
                l+=1
            else:
                res[i] = rs
                r-=1
        return res