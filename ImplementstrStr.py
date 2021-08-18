# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# For the purpose of this problem, we will return 0 when needle is an empty string.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        N = len(haystack)
        M = len(needle)
        if needle in haystack and len(needle) != 0:
            while i < N:
                if haystack[i:i+M] == needle:
                    return(i)   
                i+=1
        elif needle == "": 
            return(0)
        else:
            return(-1)
