class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        f = Counter(nums)
        for k,v in f.items():
            if v > 1:
                return k