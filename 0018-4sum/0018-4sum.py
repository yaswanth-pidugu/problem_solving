class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j!=i+1 and nums[j] == nums[j-1]:
                    continue
                k,l = j+1,len(nums)-1
                while k<l:
                    t = nums[i] + nums[j] + nums[k] + nums[l]
                    if t < target:
                        k+=1
                    elif t > target:
                        l-=1
                    else:
                        res.append([nums[i] , nums[j] , nums[k] , nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k] == nums[k-1]:
                            k+=1
                        while k<l and nums[l] == nums[l+1]:
                            l-=1
        return res