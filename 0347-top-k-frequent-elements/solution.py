from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # basically, you are given a list of numbers and an int k
        # the int k gives the k most frequent elements that will be outputted from the list of nums
        
        # first thought: go through list starting from first element, and compare to rest, if same element, then add one count for that element, and keep going and hten order and take the top k elements
        # optimal: hashmap:
        # store key value pairs where if a element has already been seen, store it in the hashmap (add 1 for that key)
        # take the top k elements from the hashmap by getting the keys, sorted by values

        count = Counter(nums)

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]
        
        
