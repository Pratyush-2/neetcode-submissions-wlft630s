class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(n):
            ans=nums
            if nums[i] == ans[i]:
                return list(ans+ans)

        