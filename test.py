# Import required module
import time


# define function to implement for loop
def for_loop(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result


# define function to implement list comprehension
def list_comprehension(n):
    return [i**2 for i in range(n)]

# function to test
def reverse(x: int) -> int:
    conv_str = str(x) #convert int to string and assign to strg
    if x >= 0:
        revstr = conv_str[::-1] # this reverses the string
    else:
        #this strips off the sign which is at iterable 0 by starting to count at 1
        tempstr = conv_str[1:]
        # then do the same operation as in line 21
        tempstr2 = tempstr[::-1]
        # this adds the negative sign back in while its a string
        revstr = "-" + tempstr2
    if int(revstr) > (2**31) or int(revstr) < ((2**31)*(-1)): return 0
    else: return int(revstr)

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
test_string = reverse(test_int)
print(test_string)
