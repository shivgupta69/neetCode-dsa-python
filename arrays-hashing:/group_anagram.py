class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # first created a dict which contains all values in list

        for s in strs: # for loop iterate into strs
            count = [0] * 26
            for c in s: # iterate inside s
                count[ord(c) - ord('a')] += 1 # aski no of alphabet's - aski no of a 
            res[tuple(count)].append(s) # stores the value as tuple (not mutable)
        return list(res.values()) # returns the list of values 