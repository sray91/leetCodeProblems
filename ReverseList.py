class Solution:
    #my original solution which does not satisfy the sign requirements
    def reverse(self, x: int) -> int:
        #use list comprehension to create a list of characters from an integer
        new_list = [character for character in str(abs(x))]
        #reverse the element order in the list
        new_list.reverse()
        #use map() and join() create a string out of the list, then convert to int
        conv_int = int("".join(map(str,new_list)))
        #test constraints
        if conv_int >= (2**31) or conv_int < ((2**31)*(-1)): return 0
        else: return conv_int

#using pop and push
    def reverse(self, x: int) -> int:
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
