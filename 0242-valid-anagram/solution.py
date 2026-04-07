class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if strings are same length
        if len(s) != len(t):
            return False

        # create dict to store frequencies of each char
        counter = {}

        # iterate through strings
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True
            
        
