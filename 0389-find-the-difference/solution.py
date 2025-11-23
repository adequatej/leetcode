class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # string t is made up of random shuffled letters from string s and one more letter at a random position 
        # so just count the length of t and hten subtract each letter of s from string t and then just find the last letter to return the last letter that was added to t 
        # use a hashmap to count each char in stirng t
        # subtract -1 if same key from string s so that if numbers of count are 0, delete key/value from HashMap, to get leftover 

        # initialize dict to store character counts
        count = {}

        # count chars in string t
        for c in t:
            count[c] = count.get(c, 0) + 1

        # substract counts for chars in string s
        for c in s:
            count[c] -= 1
            if count[c] == 0:
                del count[c]
        
        # return remaining char in dict as the difference
        return list(count.keys())[0]
        


        
