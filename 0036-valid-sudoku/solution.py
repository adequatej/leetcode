class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row unique #'s
        # same for each col
        # also check 3x3 boxes
        # determine if board is valid 
        # 1: check each row and col and iteratively compare each number to see if unique
        # 2: hashmap: store each values key once found, so that upon going to a new value and if it is a value seen before, then thats means its a duplicate
        # create dict, seen, to track seen values
        # dict is reset for each row, col, box
        # iterate through each col and row 
        # if a digit is seen twice, return false 
        # i: 0 - 8
        # j: 0 - 8
        # for each cell (i, j)

        seen = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                digit = board[i][j]

                # unique identifier for each constraint
                row_key = f"row_{i}_{digit}"
                col_key = f"col_{j}_{digit}"
                box_key = f"box_{i//3}_{j//3}_{digit}"
                # loop once through all 81 cells instead of multiple loops 
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        else:
            return True

