class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # have to take into account not only height of each bar, but also distance from each other
        # Brute force idea: try all pairs (i, j) of bars in the array, and calculate the water for each pair,
        #                   returning the maximum water among all pairs but this would be O(n^2)
        # Better way: Two Pointer -> Initialize two pointers, where at each step, 
        #                            we calculate the amount of water using the formula (j - i) * min(heights[i], heights[j])
        #                            Then we move the pointer that has the smaller height value since the amount of water depends 
        #                            only on the minimum height  

        l, r = 0, len(heights) - 1

        result = 0
        
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            result = max(result, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result            

        
