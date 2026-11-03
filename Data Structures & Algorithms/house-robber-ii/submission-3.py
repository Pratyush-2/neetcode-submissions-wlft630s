class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])

        def robb(nums):
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp[i] = max(nums[i] + dp[i-2],dp[i-1])
            return dp[n-1]
        
        case_a = nums[1:]
        case_b = nums[:-1]

        rob_a=robb(case_a)
        rob_b=robb(case_b)
        return max(rob_a,rob_b)


        