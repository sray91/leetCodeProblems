# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

# binary search algorithm
# divide the data set in half and inspect iteratively until result is found

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x==1:
            return(x)
        
        ans = 0
        mid = 0
        left = 0
        right = x - 1
        
        while left <= right:
            mid = (right + left)//2 # use floor division //
            ans = mid*mid
            # If x is greater, ignore left half
            if ans < x:
                left = mid + 1
            # If x is lesser, ignore right half
            elif ans > x:
                right = mid - 1
            else:
                return(mid)
        return(mid)            
