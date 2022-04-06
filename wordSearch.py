class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #width
        N = len(board[0])
        #height
        M = len(board)
        #length of reference word
        P = len(word)
        
        #define a helper method to call in recursion
        def helper(r,c,pos):
            #base condition -> position is greater than or equal to P
            if pos >= P:
                return True
            #make sure it's not out of bounds and the postion in the grid is a the position in the word
            elif 0 <= r < M and 0 <= c < N and board[r][c] == word[pos]:
                #store the grid position in a variable
                temp = board[r][c]
                #mark it "None" to show it's been visited
                board[r][c] = None
                #up, #down, #left, #right
                if helper(r-1,c,pos+1) or helper(r+1,c,pos+1) or helper(r,c-1,pos+1) or helper(r,c+1,pos+1):
                    return True
                #set back after recursion
                board[r][c] = temp
            return False
        
        #loop to call recursion
        for r in range(M):
            for c in range(N):
                if helper(r,c,0):
                    return True
        return False
