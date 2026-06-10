class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        srs = defaultdict(list)
        for s in strs: 
            sortedS = "".join(sorted(s))
            srs[sortedS].append(s)
        return list(srs.values())

