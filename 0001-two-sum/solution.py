class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums: list of nums
        # target: int
        # return: indices of two #'s such that add up to target 

        # brute force: iteratively go thorugh each pair and see fi they add up to target using nested loops, where otuer loop iterates first element to second to last element, and inner loop iterates next element to last element (O(n^2))

        # to get the length of the array of ints 
        n = len(nums)
        # go through first 
        for i in range(n - 1):
            # second go thoruigh for second int 
            for j in range(i + 1, n):
            # if both add up to target, return two indices
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

            


 
            

        
