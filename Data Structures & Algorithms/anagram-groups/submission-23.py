class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maped_strs = defaultdict(list)
        for s in strs: 
            sorted_map = "".join(sorted(s))
            
            maped_strs[sorted_map].append(s)

        return list(maped_strs.values())


                

    

    
