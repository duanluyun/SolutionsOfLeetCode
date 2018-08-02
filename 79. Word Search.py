class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.ExistenceHelper(board,word,i,j):
                        return True
        return False

    def ExistenceHelper(self,board,word,y,x):
        if len(word)==0:
            return True
        if y<0 or y>=len(board) or x<0 or x>=len(board[0]) or board[y][x]!=word[0]:
            return False
        temp=board[y][x]
        board[y][x]='#'
        res=self.ExistenceHelper(board,word[1:],y+1,x) or self.ExistenceHelper(board,word[1:],y-1,x) or self.ExistenceHelper(board,word[1:],y,x+1) or self.ExistenceHelper(board,word[1:],y,x-1)
        board[y][x]=temp
        return res

