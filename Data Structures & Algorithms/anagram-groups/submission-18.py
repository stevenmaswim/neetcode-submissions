class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map a sorted string to a list of its original anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 1. Sort the characters of the word to create a unique signature
            # e.g., "tea" -> ['a', 'e', 't'] -> "aet"
            sorted_key = "".join(sorted(s))
            
            # 2. Append the original word to the list matching that signature
            anagram_map[sorted_key].append(s)
            
        # 3. Return all the grouped lists
        return list(anagram_map.values())


                

    

    
