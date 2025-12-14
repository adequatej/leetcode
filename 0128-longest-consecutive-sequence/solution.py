class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # consecutive sequence: longest in order of numbers: 1, 2, 3, 4, not patterns
        # goal: find the longest sequence of numbers 
        # array is unsorted, 
        # 1: sort the array, so its in order, easily iterate through list to see if each number only adds by one,
        # issue with this, sometiems longest sequence can be like 7, 8, 9, makes difficult
        # O(n): can't do mulitple loops, at most one loop
        # so then 2: store all numbers in a set
        # run a loop to check if a number exists before it 
        # then check if the next number is in the list, if so then increase streak
        # use max(function) to compare lengths of all series and return it 
        # key idea: only begin counting a sequence once the first number of a sequence is found 

        seen = set(nums)
        longest = 0

        for num in seen:
            # only start counting if this is the beginning
            if num - 1 not in seen:
                curr_num = num
                curr_streak = 1
            # keep extending sequence forward
                while curr_num + 1 in seen:
                    curr_num += 1
                    curr_streak += 1

                # update longest streak found
                longest = max(longest, curr_streak)
            
        return longest

        
