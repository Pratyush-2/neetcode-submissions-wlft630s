class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1
        pairs = sorted(count.items(),reverse =True, key=lambda pair: pair[1])
        ans = []
        for pair in pairs[:k]:
            ans.append(pair[0])
        return ans
            
            
            
        

        