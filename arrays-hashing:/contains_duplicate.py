class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        ## at first i have created a empty set which contains only unique values.
        hashset = set()

        for n in nums:

            ## if my hashset has same value stored into it = returns true
            if n in hashset:
                return True

            hashset.add(n)
            
        return False

        ## time complexity = O(n)
