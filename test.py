# Import required module
import time
def longestCommonPrefix(strs: list[str]) -> str:
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
# Driver Code

# Calculate time takens by for_loop()
#begin = time.time()
#for_loop(10**6)
#end = time.time()

# Display time taken by for_loop()
#print('Time taken for_loop:',round(end-begin,2))

# Calculate time takens by list_comprehension()
#begin = time.time()
#list_comprehension(10**6)
#end = time.time()

# Display time taken by for_loop()
#print('Time taken for list_comprehension:',round(end-begin,2))

# display current string values
test_int = 123
test_string = "MCMXCIV"
test_list = ["leetcode","leet","lee"]

test_result = longestCommonPrefix(test_list)
print(test_result)
