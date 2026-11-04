class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,ans = [],[]
        def backtrack(i):
            if(i >= len(nums)):
                res.append(list(ans))
                return
           

            backtrack(i+1)

            ans.append(nums[i])
            backtrack(i+1)
            ans.pop()

        backtrack(0)
        return res


        