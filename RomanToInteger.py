class Solution:
    def romanToInt(self, s: str) -> int:
        # make a hashmap for lookup
        map = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        # now we want to move backwards to determine if the higher number is ahead
        # N returns an integer the length of string s
        # i is one less than N because the while loop goes to 0
        N = len(s) # len('MCMXCIV') = 7, i = 7 -1 = 6
        i = N-1
        result = 0 #initialize the result

        while i >= 0:
            # if the i value is less than the i+1 value, subtract the i values
            # example IV -> I = 1, V = 5, IV = 5-1 = 4
            # use "i < N-1" because the first iteration will filter out
            if i < N-1 and map[s[i]] < map[s[i+1]]:
                result -= map[s[i]]
            else:
                result += map[s[i]]
            i-=1
        return(result)
