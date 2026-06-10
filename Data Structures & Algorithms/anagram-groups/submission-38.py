class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        srs = defaultdict(list)
        
        for s in strs: 
            count = [0] * 26
            #creates and array of 0s with the size of 26 or 26 0s
            for c in s: 
                #iterates through the characters in s
                count[ord(c)-ord('a')] += 1
                #for the letter index that c corresponds to it will add one letter 
            srs[tuple(count)].append(s)
            #appends s (the value) to the key (tuple(count))
        return list(srs.values())
        #returns the values in srs as a list

    