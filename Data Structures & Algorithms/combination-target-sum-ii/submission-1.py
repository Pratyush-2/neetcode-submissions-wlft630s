class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(start,cur,summ):
            if (summ > target):
                return

            if (summ == target):
                res.append(list(cur))
                return

            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                cur.append(candidates[i])
                backtrack(i+1,cur,summ + candidates[i])
                cur.pop()

        backtrack(0,[],0)
        return res