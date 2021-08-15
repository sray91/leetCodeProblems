# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return("")
        elif len(strs) == 1:
            return(strs[0])
        # use the first string as a starting point to reference
        prefix = strs[0]
        previous_length = len(prefix)
        # loop through by checking the string in the second location
        for i in strs[1:]:
            # while the new string length doesn't match, remove a char from the original length
            while prefix != i[0:previous_length]:
                prefix = prefix[0:(previous_length-1)]
                previous_length -= 1
                # if it doesn't match at all, return empty string
                if previous_length == 0:
                    return("")
        return(prefix)
