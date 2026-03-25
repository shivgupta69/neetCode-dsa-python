class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

     ## first match the length of both arrays
        if len(s) != len(t):
            return False
    ## if the lenth matches sort them and match .. 
        return  sorted(s) == sorted(t)
