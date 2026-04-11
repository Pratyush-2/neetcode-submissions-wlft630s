class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights)
        r = n - 1
        max_area = 0
        while l < r:
            w = r - l
            height=min(heights[l],heights[r])
            area = w * height
            max_area = max(area,max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
      

            

        