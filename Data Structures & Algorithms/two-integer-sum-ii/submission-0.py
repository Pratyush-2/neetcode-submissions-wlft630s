class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        n = len(nums)
        r = n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l+1,r+1]
            elif s < target:
                l+=1
            elif s > target:
                r-=1

            
        
        
            
            
        