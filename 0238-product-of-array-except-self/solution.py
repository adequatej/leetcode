class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # list of nums (unsorted)
        # return list of answers
        # same number of answers as nums - 1:1
        # prefix[i] = nums[0] * nums[1]...nums[i-1]
        # suffix[i] = nums[i+1] * nums[i+2]...nums[n-1]
        # each answer[i] is equal to the product of all nums besides nums[i]
        # edge cases: if num of answers != num of elements, False
        # could there be repeating numbers?
        # 1: loop throuhg all numbers once, for each element, get the product 
        
        n = len(nums)
        result = [1] * n

        # prefix?
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
        # multiply by suffix products 
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result 
    


        
