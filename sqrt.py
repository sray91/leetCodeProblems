# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

# binary search algorithm
# divide the data set in half and inspect iteratively until result is found

class Solution:
    def mySqrt(self, x: int) -> int:
    # babylonian method
        if x == 0 or x == 1:
            return(x)
        else:
            # this is the initial estimate
            x_n = 0.5 * x
            change = 1
            while change > 0.1:
                next_n = 0.5 * (x_n + x/x_n)
                change  = abs(x_n - next_n)
                x_n = next_n
        return(int(x_n))   
