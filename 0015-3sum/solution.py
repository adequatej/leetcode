class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # list of nums, return all triplets (i, j, k) where the sum of them equal 0 (all distinct too)
        # output should not contian any duplicate triplets either, may return in any order though
        # edge cases: 
        #   length >= 3, so length < 3 return [],
        #   if all duplicates -> [0, 0, 0] only once 
        #   if all positives or all negs -> [] because can't equal 0

        # 1st approach: sort nums, and iterate through the list with a fixed number (a)
        # while skipping duplicates, use two pointers where if sum is too small, then move left pointer to right
        # if sum is too big, then move right pointer to the right 
        # if equal to 0, record as a triplet, then repeat until iteration is over. 

        nums.sort()
        result = []
        n = len(nums)

        # edge cases
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break 
            
            # initialize pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result


        
