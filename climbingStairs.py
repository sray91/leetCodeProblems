class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci sequence
        if n == 0 or n == 1 or n == 2:
            return(n)
        else:
            prev1 = 1
            prev2 = 2
            for i in range(2,n):
                current = prev1 + prev2
                prev1 = prev2
                prev2 = current
            return(current)
