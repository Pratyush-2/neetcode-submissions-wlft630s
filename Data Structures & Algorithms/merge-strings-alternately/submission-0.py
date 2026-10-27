class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        ans = ""

        while l < len(word1) and l < len(word2):
            ans += word1[l] + word2[l]
            l += 1
        if l < len(word1):
            ans += word1[l:]
        if l < len(word2):
            ans += word2[l:]
        return ans
