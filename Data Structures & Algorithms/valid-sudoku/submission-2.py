class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = True
        for row in board:
            raw_row = list(filter(lambda val: val != '.', row))
            raw_len = len(raw_row)
            set_len = len(set(raw_row))
            if raw_len != set_len:
                return False
        for i in range(9):
            col = [row[i] for row in board]
            raw_col = list(filter(lambda val: val != '.', col))
            raw_len_col = len(raw_col)
            set_len_col = len(set(raw_col))
            if raw_len_col != set_len_col:
                return False
        square_dict = collections.defaultdict(list)
        for i in range(9):
            for j in range(9):
                square = round((i//3)*3 + (j//3))
                if board[i][j] != '.':
                    square_dict[square].append(board[i][j])
        for v in square_dict.values():
            if len(set(v)) != len(v):
                return False
        return res
                
                
                
                
                
                