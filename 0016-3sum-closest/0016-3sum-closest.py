class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    l+=1
                elif total > target:
                    r-=1
                else:
                    l+=1
                    r-=1
        return closest