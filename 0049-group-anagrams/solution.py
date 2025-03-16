class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for str in strs:
            # Sort each word alphabetically
            sorted_word = ''.join(sorted(str))
            # Group words by same sorted word
            hash_map[sorted_word].append(str)
        # return grouped anagrams
        return list(hash_map.values())

            
            
        
