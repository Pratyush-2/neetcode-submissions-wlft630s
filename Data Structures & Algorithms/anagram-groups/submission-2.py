class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key ="".join(sorted(word))
            group[key] = group.get(key,[]) + [word]
        return list(group.values())
            
            

            
        
        