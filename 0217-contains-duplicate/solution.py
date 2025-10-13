class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute Force: check all elements against each other and if the same then return true (but too slow)
        # So instead use a hashmap
        # iterates thru array, checking if each element is alr in the set, if so returns true, otherwise adds element to set 
        
        # make hashset
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False



        

        
