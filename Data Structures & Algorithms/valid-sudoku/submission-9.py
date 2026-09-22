class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board :
            bucket=set()
            for number in row:
                if number==".":
                    continue
                if number in bucket:
                    return False
                bucket.add(number)
        
        for column in range(9):
            bucket=set()
            for row in range(9):
                number=board[row][column]
                if number ==".":
                    continue
                if number in bucket:
                    return False
                bucket.add(number)
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                bucket=set()
                for row in range(box_row,box_row+3):
                    for col in range(box_col,box_col+3):
                        number=board[row][col]
                        if number==".":
                            continue
                        if number in bucket :
                            return False

                        bucket.add(number)
        return True