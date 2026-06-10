class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: 
            sorted_results = ''.join(sorted(s))
            res[sorted_results].append(s)
        return list(res.values())
                

    

    
