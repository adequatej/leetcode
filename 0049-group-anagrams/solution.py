class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first thought (brute force): go thru each word and its letters and compare to all others to see if its an anagram, but gets worse as the list gets longer (O(n^2))
        # optimal: hashmap: go thru each word in strings and check if combintation of letters is already in hashmap, if so, add the word to the array associated with that key, and so on

        # initialize hashmap to store lists of grouped anagrams by a common key
        # defaultdict w/ list as default: if a key DNE in dict, creates an empty list for that key
        anagram_map = defaultdict(list)

        # iterate over each string in list to group each string w/ its anagrams
        for word in strs:
            # sort each strign to create a key
            # word is sorted into a new sorted string which 
            # acts as a unique identifier for anagrams (aet)
            sorted_word = ''.join(sorted(word))
            # group the string under its anagram key
            # word is append to the list in the dict that corresponds to its key
            # this groups all anagrams together in the same list 
            anagram_map[sorted_word].append(word)

        # return grouped anamgrams using .values method (returns list of lists)
        return list(anagram_map.values())
        
