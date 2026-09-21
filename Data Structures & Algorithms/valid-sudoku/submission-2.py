class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        check = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.':
                    row = f"Row{i}, Value-{board[i][j]}"
                    col = f"Column{j}, Value-{board[i][j]}"
                    box = f"Box{i//3}{j//3}, Value-{board[i][j]}"
                    if row in check or col in check or box in check:
                        return False
                
                    check.add(row)
                    check.add(col)
                    check.add(box)
            
        return True
        