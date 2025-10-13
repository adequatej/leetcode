from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge cases:
        # check if same length first
        # brute: sort and if each letter is hte same, then anagram
        # Hashmpa; compare frequencies
        if len(s) != len(t):
            return False

        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        
        return True
            
       
         
