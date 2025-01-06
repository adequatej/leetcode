class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = 0
        for rs in s: 
            r ^= ord(rs)
        for rt in t:
            r ^= ord(rt)
        return chr(r)
