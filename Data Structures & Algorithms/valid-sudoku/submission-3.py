class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check=set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    row=f"row:{i}-value:{board[i][j]}"
                    col=f"col:{j}-value:{board[i][j]}"
                    square=f"square:{i//3}{j//3}-value:{board[i][j]}"
                    if row in check or col in check or square in check:
                        return False
                    check.add(row)
                    check.add(col)
                    check.add(square)
        return True
