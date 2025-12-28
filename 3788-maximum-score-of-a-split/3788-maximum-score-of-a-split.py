class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        suffixMini = [0]*n
        suffixMini[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffixMini[i] = min(nums[i], suffixMini[i+1])
        prefSum = 0
        maxi = float('-inf')
        for i in range(n-1):
            prefSum += nums[i]
            score = prefSum - suffixMini[i+1]
            maxi = max(maxi,score)
        return maxi      