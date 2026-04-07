class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # check if lengths are the same
        if len(ransomNote) > len(magazine):
            return False

        # use Counter class to store the frequency counts of each string
        magazine_counts = collections.Counter(magazine)
        ransom_note_counts = collections.Counter(ransomNote)

        # iterate through ransomnote and see if for each char in ransomnote, it is in magazine and if so remove in magazine 
        for char, count in ransom_note_counts.items():
            # check that hte count of chars in magazine is equal or higher than the count in ransom note
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False
        return True
