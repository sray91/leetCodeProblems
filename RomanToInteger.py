class Solution:
    def romanToInt(self, s: str) -> int:
        List = [character for character in s]
        result = 0
        for i in range(len(List)):
            if List[i] == 'I': result+=1
            elif List[i] == 'V': result+=5
            elif List[i] == 'X': result+=10
            elif List[i] == 'L': result+=50
            elif List[i] == 'C': result+=100
            elif List[i] == 'D': result+=500
            elif List[i] == 'M': result+=1000
        return(result)
