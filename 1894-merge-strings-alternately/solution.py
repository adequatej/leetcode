class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0

        while i < len(word1) and i < len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        if len(word1) > i:
            merged.append(word1[i:])
        if len(word2) > j:
            merged.append(word2[j:])

        return "".join(merged)



       



