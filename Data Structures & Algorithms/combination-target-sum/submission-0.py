class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, cur, summ):
            if summ > target:
                return
            if summ == target:
                ans.append(list(cur))
                return
            if i >= len(nums):
                return
            cur.append(nums[i])
            backtrack(i,cur,summ + nums[i])
            cur.pop()

            backtrack(i+1,cur,summ)

        backtrack(0,[],0)
        return ans