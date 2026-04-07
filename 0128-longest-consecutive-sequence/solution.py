class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # convert array to set for O(1)  lookups
        num_set = set(nums)

        # longest will stoer best streak
        longest = 0

        # loop thoruhg each number in the set 
        for num in num_set:
            # only start counting a streak if num - 1 is NOT in the set (beginning of seq)
            if num - 1 not in num_set:
                curr_num = num # is the number we're curr checking
                curr_length = 1 # tracks how long this part. streak is 
    
                # if it is the start, keep checking if num+1 exists in the set (count up length of that streak)
                while curr_num + 1 in num_set:
                    # go to next num
                    curr_num += 1

                    # increment lenght of the curr_streak
                    curr_length += 1
                
                 # update longest if streak beats it
                longest = max(longest, curr_length)

         # return longest consecutive sequence lenght found
        return longest if longest > 0 else 0
