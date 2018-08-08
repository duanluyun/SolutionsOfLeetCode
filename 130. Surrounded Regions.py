class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == None:
            return None
        if len(board) >= 1 and len(board[0]) >= 1:
            numRows = len(board)
            numCols = len(board[0])
            req = []
            for y in range(numRows):
                for x in range(numCols):
                    if board[y][x] == 'O':
                        if y == 0 or y == numRows - 1 or x == 0 or x == numCols - 1:
                            req.append((y, x))
            while req:
                r, l = req.pop(0)
                board[r][l] = 'D'
                if r - 1 >= 0 and board[r - 1][l] == 'O':
                    req.append((r - 1, l))
                if r + 1 <= numRows - 1 and board[r + 1][l] == 'O':
                    req.append((r + 1, l))
                if l - 1 >= 0 and board[r][l - 1] == 'O':
                    req.append((r, l - 1))
                if l + 1 <= numCols - 1 and board[r][l + 1] == 'O':
                    req.append((r, l + 1))

            for y in range(numRows):
                for x in range(numCols):
                    board[y][x] = 'O' if board[y][x] == 'D' else 'X'
