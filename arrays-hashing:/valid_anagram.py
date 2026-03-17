class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ## at first i will verify the length of s = t.
        ## if not same returns false.
        if len(s) != len(t):
            return False

        ## is the length is same then
        ## I will sort them and match with each other 
        
        ## if it matches s = t then return true.
        return  sorted(s) == sorted(t)